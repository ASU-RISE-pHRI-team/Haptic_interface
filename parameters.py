import numpy as np


class Parameters1:
    # System dynamic parameters
    num_player = 2
    dim_state = 6
    dim_input = 2
    m = 0.2
    a = 0.3
    b = 2
    length = 0.5 * b
    inertia = 0.067
    ft = 0.02
    fr = 0.0067
    T = 0.1
    # goal position
    x0 = np.array([0, 4, 0, 0, 0, 0])
    # goal_set  = np.array([1,0,0,0,-np.pi * 0.5,0])
    # initial state
    goal = np.array([0, 0, 0, 0, 0, 0])
    # weigh matrix
    w1 = 1e5
    w2 = 1
    w3 = 1e3
    w4 = 1
    P = np.array([[4, 0, 0.3, 0.1, 0, 0], [0, 4, 0.1, 0.3, 0, 0], [0.3, 0.1, 1, 0.1, 0, 0], [0.1, 0.3, 0.1, 1, 0, 0], [0, 0, 0, 0, 9, 0.3], [0, 0, 0, 0, 0.3, 1]])
    H = 50
    theta1 = 1e-3
    theta2 = 1e-3
