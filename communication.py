import threading
import zmq
import json
import numpy as np
import time
from optimal_agent import Optimalagent
from parameters import Parameters1


class Communication:

    def __init__(self):
        self.context1 = zmq.Context()
        self.context2 = zmq.Context()
        self.context3 = zmq.Context()
        self.socket_in1 = self.context1.socket(zmq.SUB)
        self.socket_in2 = self.context2.socket(zmq.SUB)
        self.socket_out = self.context3.socket(zmq.PUB)
        self.socket_in1.connect("tcp://127.0.0.1:5557")
        self.socket_in2.connect("tcp://127.0.0.1:5527")
        self.socket_out.bind("tcp://127.0.0.1:7001")

        self.rec_1 = threading.Thread(target=self.rec1)
        self.rec_2 = threading.Thread(target=self.rec2)

        # self.sender = threading.Thread(target=self.send)
        self.quad_thread = threading.Thread(target=self.run_sth)
        self.quad_thread.daemon = True
        self.forces = {"force_x": -5.0, "force_y": 0, "force_z": 0}
        self.loc = 0
        # self.pos = 0
        # self.r = 0
        # self.v = 0
        # self.w = 0
        self.state = Parameters1.x0
        self.msg = {"force_x": -10.0, "force_y": 0, "force_z": 0}
        self.observed_action = []

    def rec1(self):

        topic_filter = b""
        self.socket_in1.setsockopt(zmq.SUBSCRIBE, topic_filter)
        while True:
            forces = self.socket_in1.recv_string()
            self.forces = json.loads(forces)

            # self.forces =
            # print(self.forces)

    def rec2(self):

        topic_filter = b""
        self.socket_in2.setsockopt(zmq.SUBSCRIBE, topic_filter)
        while True:
            self.loc = self.socket_in2.recv_string()
            # print(self.loc)

    def send(self, msg):
        # while True:
        #     #message = json.dumps(msg)
        self.socket_out.send_string(msg)
        # print(msg)

    def runner1(self):
        self.rec_1.start()

    def runner2(self):
        self.rec_2.start()

    #  def my_sender(self, msg):
    #      self.send(msg)

    def run_sth(self):
        while True:
            time.sleep(0.05)

    def run(self):
        self.quad_thread.start()

    def translate(self):
        jmsg = json.loads(self.loc)
        jr = jmsg["Rotation"]
        jp = jmsg["Position"]
        jw = jmsg["Angularvelocity"]
        jv = jmsg["Velocity"]
        # self.pos = np.array(jp)
        # self.r = np.array(jr)
        # self.w = np.array(jw)
        # self.v = np.array(jv)
        self.state = np.array([jp[0], jp[2], jv[0], jv[2], jr[1] / 180 * np.pi, jw[1]])
        self.observed_action = self.forces["force_x"]

        # return self.pos, self.r, self.v, self.w

    def msg_gen(self, action):

        msg = {"force_x": action, "force_y": 0, "force_z": 0}

        return msg


def main():
    agent = Optimalagent(Parameters1)
    kim = Communication()
    kim.run()
    kim.runner1()
    kim.runner2()
    time.sleep(3)
    print(kim.state)
    while True:
        t1 = time.time()
        # msg_dic = kim.forces
        # msg_json = json.dumps(msg_dic)
        kim.translate()
        agent.state = kim.state
        agent.other_action = kim.observed_action
        A, B1, B2 = agent.sys_gen()
        U = agent.optimal_action(A, B1, B2)
        msg = kim.msg_gen(U[0])
        msg_json = json.dumps(msg)
        kim.send(msg_json)
        # agent.agentlearning(A, B1, B2, U[0], kim.observed_action)
        t2 = time.time()
        if t2 - t1 - 0.05 < 0:
            time.sleep(0.05 - t2 + t1)


if __name__ == '__main__':
    main()
