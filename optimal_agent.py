import numpy as np


class Optimalagent:

    def __init__(self, constants):
        self.mass = constants.m
        self.I = constants.inertia
        self.fric_t = constants.ft
        self.fric_r = constants.fr
        self.length = constants.length
        self.state = constants.x0
        self.state_set = [self.state]
        self.other_action = []
        self.other_action_set = []
        self.action = []
        self.action_set = []
        self.goal = constants.goal
        self.T = constants.T
        self.P = constants.P
        self.N = constants.dim_state
        self.r = constants.dim_input
        self.num = constants.num_player
        self.theta1 = constants.theta1
        self.theta2 = constants.theta2
        self.theta1_hat = 1e-3
        self.theta2_hat = 1e-3
        self.timer = []
        self.reaction = []
        self.reaction_set = []

    def sys_gen(self):
        theta = self.state[4]
        T = self.T
        cfr1 = self.fric_t
        cfr2 = self.fric_r
        M = self.mass
        l = self.length
        I = self.I
        A = np.array(
            [[1, 0, T, 0, 0, 0], [0, 1, 0, T, 0, 0], [0, 0, (1 - cfr1 * T / M), 0, 0, 0],
             [0, 0, 0, (1 - cfr1 * T / M), 0, 0], [0, 0, 0, 0, 1, T], [0, 0, 0, 0, 0, (1 - cfr2 * T / I)]])
        # B1 = np.array([[0], [0], [np.cos(theta) * T / M], [np.cos(theta) * T / M], [0], [T * l / I]])
        # B2 = np.array([[0], [0], [np.cos(theta) * T / M], [np.cos(theta) * T / M], [0], [-T * l / I]])
        B1 = np.array(
            [[0, 0], [0, 0], [T / M, 0], [0, T / M], [0, 0], [np.sin(theta) * T * l / I, -np.cos(theta) * T * l / I]])
        B2 = np.array(
            [[0, 0], [0, 0], [T / M, 0], [0, T / M], [0, 0], [-np.sin(theta) * T * l / I, np.cos(theta) * T * l / I]])

        return A, B1, B2

    def state_update(self, A, B1, B2, u1, u2):
        old_state = self.state
        new_state = np.dot(A, old_state) + np.dot(B1, u1) + np.dot(B2, u2)
        return new_state

    def optimal_action(self, A, B1, B2):
        P = self.P
        B = np.hstack((B1, B2))
        BP = np.matmul(B.transpose(), P)
        BPB = np.matmul(BP, B)

        R = self.thetator(self.theta1, self.theta1)
        if np.linalg.det(R + BPB) == 0:
            u = np.array([0, 0])
        else:
            inv = np.linalg.inv(R + BPB)
            res1 = np.matmul(P, A)
            res2 = np.matmul(B.transpose(), res1)
            res3 = np.matmul(res2, self.state)
            u = -np.matmul(inv, res3)
        return u

    def blame_all(self, A, B1, B2):
        P = self.P
        B = np.hstack((B1, B2))
        BP = np.matmul(B.transpose(), P)
        BPB = np.matmul(BP, B)
        R_hat = self.thetator(self.theta1_hat, self.theta2_hat)
        H1 = np.diag(np.diag(BPB)) + self.thetator(self.theta1, self.theta2)
        # H1 = np.diag(np.diag(BPB)) + R_hat
        H2 = BPB - H1

        inv = np.linalg.inv(R_hat + BPB)
        res1 = np.matmul(P, A)
        res2 = np.matmul(B.transpose(), res1)
        res3 = np.matmul(res2, self.state)
        u_hat = -np.matmul(inv, res3)
        P1 = - np.matmul(np.linalg.inv(H1), res3)
        P2 = -np.matmul(np.linalg.inv(H1), H2)
        u = P1 + np.matmul(P2, u_hat)
        return u

    def thetator(self, theta1, theta2):
        N = self.r
        P = self.num
        theta = np.array([theta1, theta2])
        r = np.array([])
        for i in range(P):
            r = np.append(r, np.ones(N) * theta[i])
        R = np.diag(r)
        return R

    def state_reg(self, world_state):
        regulator_state = world_state - self.goal
        return regulator_state

    def agentlearning(self, A, B1, B2, u1, u2):

        x = self.state
        P = self.P
        B = np.hstack((B1, B2))
        BP = np.matmul(B.transpose(), P)
        BPB = np.matmul(BP, B)
        R_hat = self.thetator(self.theta1_hat, self.theta2_hat)
        inv = np.linalg.inv(R_hat + BPB)
        res1 = np.matmul(inv, BP)
        res2 = np.matmul(res1, A)
        Uhat = np.matmul(res2, x)
        xhat1 = self.state_update(A, B1, B2, Uhat[0:2] - u1, Uhat[2:4])
        xhat2 = self.state_update(A, B1, B2, Uhat[0:2], Uhat[2:4] - u2)
        res3_p1 = np.dot(P, xhat1)
        res3_p2 = np.dot(P, xhat2)
        norm1 = (np.linalg.norm(u1)) ** 2
        norm2 = (np.linalg.norm(u2)) ** 2
        theta1_hat_new = - np.dot(np.dot(B1, u1), res3_p1) / norm1
        theta2_hat_new = - np.dot(np.dot(B2, u2), res3_p2) / norm2

        self.theta1_hat = theta1_hat_new
        self.theta2_hat = theta2_hat_new

    def data_append(self, x, other_action, reaction, time):
        self.state = x
        self.state_set.append(x)
        self.other_action = other_action
        self.reaction = reaction
        self.other_action_set.append(other_action)
        self.action_set.append(self.action)
        self.reaction_set.append(self.reaction)
        self.timer.append(time)

    def input_o2g(self, action):
        theta = self.state[4] + 0.5 * np.pi
        local_action = np.array([np.cos(theta) * action[0] + -np.sin(theta) * action[1],
                                 np.sin(theta) * action[0] + np.cos(theta) * action[1]])
        return local_action

    def input_g2o(self, action):
        theta = - (self.state[4] + 0.5 * np.pi)
        global_action = np.array([np.cos(theta) * action[0] + -np.sin(theta) * action[1],
                                  np.sin(theta) * action[0] + np.cos(theta) * action[1]])
        return global_action
