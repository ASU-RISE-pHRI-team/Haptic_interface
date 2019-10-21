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
        self.action = []
        self.action_set = []
        self.goal = constants.goal
        self.T = constants.T
        self.P = constants.P
        self.N = constants.dim_state
        self.num = constants.num_player
        self.theta1 = constants.theta1
        self.theta2 = constants.theta2

    def sys_gen(self):
        theta = self.state[4]
        T = self.T
        cfr1 = self.fric_t
        cfr2 = self.fric_r
        M = self.mass
        l = self.length
        I = self.I
        A = np.array([[1, 0, T, 0, 0, 0], [0, 1, 0, T, 0, 0], [0, 0, (1-cfr1/M), 0, 0, 0], [0, 0, 0, (1-cfr1/M), 0, 0], [0, 0, 0, 0, 1, T],[0, 0, 0, 0, 0, 1-cfr2/I]])
        B1 = np.array([[0], [0], [np.cos(theta)*T/M], [np.cos(theta)*T/M], [0], [T*l/I]])
        B2 = np.array([[0], [0], [np.cos(theta)*T/M], [np.cos(theta)*T/M], [0], [-T*l/I]])
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
        R = self.thetatoR(self.theta1, self.theta2)
        if np.linalg.det(R+BPB) == 0:
            u = np.array([0, 0])
        inv = np.invert(R+BPB)
        res1 = np.matmul(P, A)
        res2 = np.matmul(B.transpose(), res1)
        u = -np.matmul(inv, res2)
        return u


    def thetatoR(self, theta1, theta2):
        N = self.N
        P = self.num
        r = np.array([])
        for i in range(P):
            np.append(r, np.ones(N))
        R = np.diag(r)
        return R