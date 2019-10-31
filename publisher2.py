import zmq
import json
import time


class Communication:

    def __init__(self):
        self.context = zmq.Context()
        self.socket_out = self.context.socket(zmq.PUB)
        self.socket_out.bind("tcp://*:5571")

    def send(self, msg):
        self.socket_out.send_string(msg)


def main():
    mac = Communication()
    while True:
        m = {"force_x": -5.0, "force_y": 0, "force_z": 0}
        # msg = json.dumps(m)
        # time.sleep(1)
        # j_msg = json.load(msg)
        # fx = j_msg["force_x"]
        # fy = j_msg["force_y"]
        # fz = j_msg["force_z"]
        # print(fx)
        #my_msg = {"force_x": fx, "force_y": fy, "force_z": fz}
        data = json.dumps(m)
        print(data)
        mac.send(data)


if __name__ == '__main__':
    main()
