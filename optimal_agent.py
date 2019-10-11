import numpy as np


class Optimalagent:

    def __init__(self, constants):
        self.mass = constants.m
        self.I = constants.I
        self.fric_t = constants.ft
        self.fric_r = constants.fr
        self.length = constants.l
        self.state = constants.x0
        self.action = []



    def
