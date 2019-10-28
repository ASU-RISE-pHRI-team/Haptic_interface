import zmq
import json


class Communication:

    def __init__(self):
        self.context = zmq.Context()
        self.socket_out = self.context.socket(zmq.PUB)
        self.socket_out.bind("tcp://*:5572")

    def send(self, msg):
        self.socket_out.send_string(msg)


def main():
    mac = Communication()
    while True:
        my_msg = {"pos_x": -5.0, "pos_y": -2.0, "pos_z": 0}
        data = json.dumps(my_msg)
        mac.send(data)


if __name__ == '__main__':
    main()
