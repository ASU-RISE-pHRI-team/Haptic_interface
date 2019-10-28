import threading
import zmq
import json



class Communication:

    def __init__(self):
        self.context1 = zmq.Context()
        self.context2 = zmq.Context()
        self.socket_in1 = self.context1.socket(zmq.SUB)
        self.socket_in2 = self.context2.socket(zmq.SUB)
        self.rec_1 = threading.Thread(target=self.rec1)
        self.rec_2 = threading.Thread(target=self.rec2)
        self.quad_thread = threading.Thread(target=self.run_sth)
        self.quad_thread.daemon = True
        self.a = 1
        self.msg1 = 0
        self.msg2 = 0

    def rec1(self):
        self.socket_in1.connect("tcp://localhost:5571")
        topic_filter = b""
        self.socket_in1.setsockopt(zmq.SUBSCRIBE, topic_filter)
        while True:
            self.msg1 = self.socket_in1.recv_string()
            print(self.msg1)

    def rec2(self):
        self.socket_in2.connect("tcp://localhost:5572")
        topic_filter = b""
        self.socket_in2.setsockopt(zmq.SUBSCRIBE, topic_filter)
        while True:
            self.msg2 = self.socket_in2.recv_string()
            print(self.msg2)

    def runner1(self):
        self.rec_1.start()

    def runner2(self):
        self.rec_2.start()

    def run_sth(self):
        while True:
            self.a = self.a + 1

    def run(self):
        self.quad_thread.start()


def main():
    kim = Communication()
    kim.run()
    kim.runner1()
    kim.runner2()


if __name__ == '__main__':
    main()
