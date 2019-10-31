import zmq
import json
import time


# class Communication:
#
#     def __init__(self):
#         self.context = zmq.Context()
#         self.socket_out = self.context.socket(zmq.PUB)
#         self.socket_out.bind("tcp://*:5558")
#         # self.context = zmq.Context()
#         # self.socket_in = self.context.socket(zmq.SUB)
#         # self.socket_in.connect("tcp://localhost:5557")
#
#     # def rec(self):
#     #     topic_filter = b""
#     #     self.socket_in.setsockopt(zmq.SUBSCRIBE, topic_filter)
#     #     msg = self.socket_in.recv_string()
#     #     return msg
#
#     def send(self, msg):
#         #  Send reply back to client
#         self.socket_out.send_string(msg)
#
#
# def main():
#     mac = Communication()
#     while True:
#         # data = mac.rec()
#         my_msg = {"force_x": -5.0, "force_y": 0, "force_z": 0}
#         data = json.dumps(my_msg)
#         mac.send(data)
#
#
# if __name__ == '__main__':
#     main()

class Forces:
    def __init__(self):
        context = zmq.Context()
        self.socket_in = context.socket(zmq.SUB)
        self.socket_out = context.socket(zmq.PUB)
        self.socket_in.connect("tcp://localhost:5557")
        self.socket_out.bind("tcp://*:5571")

    def rec(self):
        topic_filter = b""
        self.socket_in.setsockopt(zmq.SUBSCRIBE, topic_filter)
        msg = self.socket_in.recv_string()
        return msg

    def send(self, data):
        #  Send reply back to client
        self.socket_out.send_string(data)


while True:
    tim = Forces()
    message_1 = tim.rec()
    time.sleep(1)
    tim.send(message_1)
