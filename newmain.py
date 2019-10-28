import get_location
import zmq
import time
import threading
import json
import numpy as np


class Receiver:

    def __init__(self):
        self.port = "5557"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.subport = "5527"
        self.contextsub = zmq.Context()
        self.subsocket = self.contextsub.socket(zmq.SUB)
        self.receive_thread = threading.Thread(target=self.recvdata)
        self.quad_thread = threading.Thread(target=self.run_sth)

    def setup_comm(self):
        self.socket.bind("tcp://localhost*:%s" % self.port)

        self.quad_thread.daemon = True

        # self.receive_thread = threading.Thread(target=self.recvdata)
        # self.quad_thread = threading.Thread(target=self.run_sth)
        # self.quad_thread.daemon = True

    def recvdata(self):
        topic_filter = b""
        self.subsocket.setsockopt(zmq.SUBSCRIBE, topic_filter)
        self.subsocket.connect("tcp://localhost:5527")
        while True:
            data = self.subsocket.recv_string()
            jmsg = json.loads(data)
            jr = jmsg["Rotation"]
            jp = jmsg["Position"]
            jw = jmsg["Angularvelocity"]
            jv = jmsg["Velocity"]
            pos = np.array(jp)
            r = np.array(jr)
            w = np.array(jw)
            v = np.array(jv)
            return pos, r, w, v

    def run_sth(self):
        pass

    def runsub(self):
        self.receive_thread.start()

    def run(self):
        self.quad_thread.start()

    def recv_data(self):
        topic_filter = b""
        self.socket.setsockopt(zmq.SUBSCRIBE, topic_filter)
        msg = self.socket.recv_string()
        return msg

    def my_recvr(self):
        self.run()
        self.runsub()
        while True:
            val = self.recv_data()
            return val


class Sender:
    def __init__(self):
        self.newcontext = zmq.Context()
        self.socket_out = self.newcontext.socket(zmq.PUB)
        self.socket_out.bind("tcp://*:5578")

    def send(self, data):
        #  Send reply back to client
        self.socket_out.send_string(data)


def main():
    player = Receiver()
    s_player = Sender()

    while True:
        msg1 = player.my_recvr()
        print(msg1)
        pos, rot, vel, r_vel = player.recvdata()
        print(pos, rot, vel, r_vel)
    # data = 'Hello'
    # s_player.send(data)


if __name__ == '__main__':
    main()
