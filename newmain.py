import threading
import zmq
import json
import numpy as np
import time


class Communication:

    def __init__(self):
        self.context1 = zmq.Context()
        self.context2 = zmq.Context()
        self.context3 = zmq.Context()
        self.socket_in1 = self.context1.socket(zmq.SUB)
        self.socket_in2 = self.context2.socket(zmq.SUB)
        self.socket_out = self.context3.socket(zmq.PUB)
        self.rec_1 = threading.Thread(target=self.rec1)
        self.rec_2 = threading.Thread(target=self.rec2)
        self.sender = threading.Thread(target=self.send)
        self.quad_thread = threading.Thread(target=self.run_sth)
        self.quad_thread.daemon = True
        self.a = 1
        self.forces = 0
        self.loc = 0
        self.pos = 0
        self.r = 0
        self.v = 0
        self.w = 0
        self.msg = {"force_x": -10.0, "force_y": 0, "force_z": 0}

    def rec1(self):
        self.socket_in1.connect("tcp://localhost:5557")
        topic_filter = b""
        self.socket_in1.setsockopt(zmq.SUBSCRIBE, topic_filter)
        while True:
            self.forces = self.socket_in1.recv_string()
            print(self.forces)

    def rec2(self):
        self.socket_in2.connect("tcp://localhost:5527")
        topic_filter = b""
        self.socket_in2.setsockopt(zmq.SUBSCRIBE, topic_filter)
        while True:
            self.loc = self.socket_in2.recv_string()
            print(self.loc)

    def send(self, msg):
        self.socket_out.bind("tcp://*:5572")
        while True:
            message = json.dumps(msg)
            self.socket_out.send_json(message)

    def runner1(self):
        self.rec_1.start()

    def runner2(self):
        self.rec_2.start()

    def my_sender(self, message):
        self.send(message)

    def run_sth(self):
        while True:
            self.a = self.a + 1

    def run(self):
        self.quad_thread.start()

    def translate(self):
        jmsg = json.loads(self.loc)
        jr = jmsg["Rotation"]
        jp = jmsg["Position"]
        jw = jmsg["Angularvelocity"]
        jv = jmsg["Velocity"]
        self.pos = np.array(jp)
        self.r = np.array(jr)
        self.w = np.array(jw)
        self.v = np.array(jv)
        return self.pos, self.r, self.v, self.w


def main():
    kim = Communication()
    kim.run()
    kim.runner1()
    kim.runner2()
    kim.my_sender(kim.forces)


if __name__ == '__main__':
    main()
