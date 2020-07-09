import threading
import zmq
import json
import numpy as np
import time
from optimal_agent import Optimalagent
from parameters import Parameters1
from communication import Communication


class Rec_data:

    def __init__(self):
        self.context1 = zmq.Context()
        self.context2 = zmq.Context()
        self.context3 = zmq.Context()
        self.context4 = zmq.Context()
        self.socket_in1 = self.context1.socket(zmq.SUB)
        self.socket_in2 = self.context2.socket(zmq.SUB)
        #  self.socket_out1 = self.context3.socket(zmq.PUB)
        #  self.socket_out2 = self.context4.socket(zmq.PUB)  # pallavi
        self.socket_in1.connect("tcp://localhost:1500")
        self.socket_in2.connect("tcp://localhost:1503")
        #   self.socket_out1.bind("tcp://127.0.0.1:8000")
        #   self.socket_out2.bind("tcp://127.0.0.1:8001") #pallavi

        self.rec_1 = threading.Thread(target=self.rec1)
        self.rec_2 = threading.Thread(target=self.rec2)

        # self.sender = threading.Thread(target=self.send)
        self.quad_thread = threading.Thread(target=self.run_sth)
        self.quad_thread.daemon = True
        self.forces = {"force_x": 0, "force_y": 0, "force_z": 0}
        self.loc = 0
        # self.pos = 0
        # self.r = 0
        # self.v = 0
        # self.w = 0
        self.state = Parameters1.x0
        self.msg = {"force_x": -10.0, "force_y": 0, "force_z": 0}
        self.observed_action = []
        self.other_action = []

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

    def my_sender(self, msg):  # pallavi
        self.socket_out2.send_string(msg)

    def send(self, msg):
        # while True:
        #     #message = json.dumps(msg)
        self.socket_out1.send_string(msg)
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
        if jr[1] > 180:
            angle = jr[1] - 360
        else:
            angle = jr[1]
        self.state = np.array([jp[0], jp[2], jv[0], jv[2], -angle / 180 * np.pi, -jw[1]])
        self.observed_action = np.array([self.forces["force_x"], -self.forces["force_z"]])

        # return self.pos, self.r, self.v, self.w

    def msg_gen(self, action):
        if len(action) == 1:

            msg = {"force_x": action, "force_y": 0, "force_z": 0}
        elif len(action) == 2:

            msg = {"force_x": action[0], "force_y": 0, "force_z": action[1]}

        return msg


def main():
    global agent
    global kim
    agent = Optimalagent(Parameters1)
    kim = Rec_data()
    try:

        kim.run()
        kim.runner1()
        kim.runner2()
        time.sleep(3)
        # print(kim.state)
        state_set = [kim.state]
        action_1 = -1.0
        action_2 = 1.0

        while True:
            t1 = time.time()
            kim.translate()
            agent.state = kim.state

            print(kim.observed_action)

            t2 = time.time()
            agent.data_append(kim.state, kim.observed_action, t2)
            if t2 - t1 - Parameters1.T < 0:
                time.sleep(Parameters1.T - t2 + t1)
    except KeyboardInterrupt:

        np.savetxt("/home/rise/PycharmProjects/Haptic_interface/new_data/state.csv", agent.state_set, delimiter=",")
        np.savetxt("/home/rise/PycharmProjects/Haptic_interface/new_data/action_h1.csv", agent.other_action_set, delimiter=",")
        np.savetxt("/home/rise/PycharmProjects/Haptic_interface/new_data/time_h1.csv", agent.timer, delimiter=",")


if __name__ == '__main__':
    main()
