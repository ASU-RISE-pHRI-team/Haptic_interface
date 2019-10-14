import numpy as  np

class Parameters1:

    # System dynamic parameters
    m = 0.2
    a = 0.3
    b = 2
    l = 0.5 * b
    I = 0.067
    ft = 0.02
    fr = 0.0067
    T = 0.01
    # goal position
    goal = np.array([1, 0, 0, 0, -np.pi * 0.5, 0])
    # goal_set  = np.array([1,0,0,0,-np.pi * 0.5,0])
    # initial state
    x0 = np.array([0, 0, 0, 0, 0, 0])
