import zmq
import json


class Communication:

    def __init__(self):
        self.context = zmq.Context()
        self.socket_out = self.context.socket(zmq.PUB)
        self.socket_out.bind("tcp://*:5571")

    def send(self, msg):
        #  Send reply back to client
        self.socket_out.send_string(msg)


def main():
    mac = Communication()
    while True:
        my_msg = {"force_x": -10.0, "force_y": 0, "force_z": 0}
        data = json.dumps(my_msg)
        mac.send(data)


if __name__ == '__main__':
    main()
