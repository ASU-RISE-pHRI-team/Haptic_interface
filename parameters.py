import numpy as np


class Parameters1:
    # System dynamic parameters
    num_player = 2
    dim_state = 6
    m = 0.2
    a = 0.3
    b = 2
    length = 0.5 * b
    inertia = 0.067
    ft = 0.02
    fr = 0.0067
    T = 0.01
    # goal position
    x0 = np.array([1, 0, 0, 0, np.pi * 0.5, 0])
    # goal_set  = np.array([1,0,0,0,-np.pi * 0.5,0])
    # initial state
    goal = np.array([0, 0, 0, 0, 0, 0])
    # weigh matrix
    w1 = 1e5
    w2 = 1
    w3 = 40
    w4 = 1
    P = np.diag([w1, w1, w2, w2, w3, w4])
    H = 50
    theta1 = 1
    theta2 = 1
