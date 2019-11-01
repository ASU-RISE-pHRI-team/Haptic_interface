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
        self.num = constants.num_player
        self.theta1 = constants.theta1
        self.theta2 = constants.theta2
        self.theta1_hat = 1
        self.theta2_hat = 1

    def sys_gen(self):
        theta = self.state[4]
        T = self.T
        cfr1 = self.fric_t
        cfr2 = self.fric_r
        M = self.mass
        l = self.length
        I = self.I
        A = np.array(
            [[1, 0, T, 0, 0, 0], [0, 1, 0, T, 0, 0], [0, 0, (1 - cfr1 / M), 0, 0, 0], [0, 0, 0, (1 - cfr1 / M), 0, 0],
             [0, 0, 0, 0, 1, T], [0, 0, 0, 0, 0, 1 - cfr2 / I]])
        B1 = np.array([[0], [0], [np.cos(theta) * T / M], [np.cos(theta) * T / M], [0], [T * l / I]])
        B2 = np.array([[0], [0], [np.cos(theta) * T / M], [np.cos(theta) * T / M], [0], [-T * l / I]])
        return A, B1, B2

    def state_update(self, A, B1, B2, u1, u2):
        old_state = self.state
        new_state = np.multiply(A, old_state) + np.multiply(u1, B1) + np.multiply(u2, B2)
        return new_state

    def optimal_action(self, A, B1, B2):
        P = self.P
        B = np.hstack((B1, B2))
        BP = np.matmul(B.transpose(), P)
        BPB = np.matmul(BP, P)
        R = self.thetator(self.theta1, self.theta2)
        if np.linalg.det(R + BPB) == 0:
            u = np.array([0, 0])
        else:
            inv = np.linalg.inv(R + BPB)
            res1 = np.matmul(P, A)
            res2 = np.matmul(B.transpose(), res1)
            u = -np.matmul(inv, res2)
        return u

    def thetator(self, theta1, theta2):
        N = self.N
        P = self.num
        theta = np.array([theta1, theta2])
        r = np.array([])
        for i in range(P):
            np.append(r, np.ones(N) * theta[i])
        R = np.diag(r)
        return R

    def state_reg(self, world_state, goal):
        regulator_state = world_state - goal
        return regulator_state

    def agentlearning(self, A, B1, B2, u1, u2):

        x = self.state
        P = self.P
        B = np.hstack((B1, B2))
        BP = np.matmul(B.transpose(), P)
        BPB = np.matmul(BP, P)
        R_hat = self.thetator(self.theta1_hat, self.theta2_hat)
        inv = np.linalg.inv(R_hat + BPB)
        res1 = np.matmul(inv, BP)
        res2 = np.matmul(res1, A)
        Uhat = np.matmul(res2, x)
        xhat = self.state_update(A, B1, B2, Uhat[0] - u1, Uhat[1] - u2)
        res3 = np.matmul(P, xhat)
        norm1 = (np.linalg.norm(u1)) ^ 2
        norm2 = (np.linalg.norm(u2)) ^ 2
        theta1_hat_new = - np.matmul(B1.transpose() * u1, res3) / norm1
        theta2_hat_new = - np.matmul(B2.transpose() * u2, res3) / norm2
        return theta1_hat_new, theta2_hat_new


    def data_append(self, x, otheraction):
        self.state = x
        self.state_set.append(x)
        self.other_action = otheraction
        self.other_action_set.append(otheraction)
