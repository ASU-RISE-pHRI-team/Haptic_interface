import zmq
import numpy as np
import math as m
import json


class Communication:

    def __init__(self):
        context = zmq.Context()
        self.socket_in = context.socket(zmq.SUB)
        #self.socket_out = context.socket(zmq.PUB)
        self.socket_in.connect("tcp://localhost:5527")
    #    self.socket_out.bind("tcp://*:5567")

        #self.socket_in.connect("tcp://localhost:5527")
        #self.socket_out.bind("tcp://*:5528")

    def rec(self):
        topic_filter = b""
        self.socket_in.setsockopt(zmq.SUBSCRIBE, topic_filter)
        msg = self.socket_in.recv_string()
        return msg

    # def send(self, data):
    #     #  Send reply back to client
    #     self.socket_out.send_string(data)

    def translate(self):
        msg = Communication.rec(self)
        jmsg = json.loads(msg)
        jr = jmsg["Rotation"]
        jp = jmsg["Position"]
        jw = jmsg["Angularvelocity"]
        jv = jmsg["Velocity"]
        pos = np.array(jp)
        r = np.array(jr)
        w = np.array(jw)
        v = np.array(jv)
        return pos, r, v, w
