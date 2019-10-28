import zmq
import json


class Communication:

    def __init__(self):
        context = zmq.Context()
        # self.socket_in = context.socket(zmq.PUB)
        self.socket_out = context.socket(zmq.PUB)
        # self.socket_out.bind("tcp://:4411")
        self.socket_out.bind("tcp://*:5571")

    def send(self, msg):
        #  Send reply back to client
        self.socket_out.send_string(msg)


mac = Communication()
while True:
    # my_msg = {"force_x": -10.0, "force_y": 0, "force_z": 0}
    # data = json.dumps(my_msg)
    data = "Hi"
    mac.send(data)
