import get_forces
from datetime import datetime
from optimal_agent import Optimalagent
import time
import get_location
import zmq
import json
import random


class Forces:
    def __init__(self):
        context = zmq.Context()
        self.socket_in = context.socket(zmq.SUB)
        self.socket_out = context.socket(zmq.PUB)
        self.socket_in.connect("tcp://localhost:5557")
        self.socket_out.bind("tcp://:5511")

    def rec(self):
        topic_filter = b""
        self.socket_in.setsockopt(zmq.SUBSCRIBE, topic_filter)
        msg = self.socket_in.recv_string()
        return msg

    def send(self, data):
        #  Send reply back to client
        self.socket_out.send_string(data)


print('Start')
communicator_1 = get_location.Communication()
communicator_2 = get_forces.Communication()
communicator_3 = Forces()
# controller = Optimalagent()
T = 0.05
while True:
    t1 = time.time()
    message_1 = communicator_1.rec()
    #message_2 = communicator_2.rec()
    message_3 = communicator_3.rec()
    print('hello')
    print(message_3)
    # print(message_1)
    # my_msg = {"force_x": -10.0, "force_y": 0, "force_z": 0}
    # data_out = json.dumps(my_msg)
    # current date and time
    # now = datetime.now().isoformat(timespec='microseconds')
    # print("timestamp =", now)
    # timestamp = datetime.timestamp(now)
    # print("timestamp =", timestamp)
    # my_msg = {"force_x": -10.0, "force_y": 0, "force_z": 0}
    # data_out = json.dumps(my_msg)
    # data_out = 'Hello'
    # communicator_3.send(data_out)
    # print('Hi')
    pos, rot, vel, r_vel = communicator_1.translate()
    # print("Position of the block =", pos)
    # print("Velocity of the block =", vel)
    # print("Angular position of the block =", rot)
    # print("Angular velocity of the block =", r_vel)

    t2 = time.time()

    # if t2 - t1 > 0:
    #     print(T - (t2 - t1))
    #     time.sleep(T - (t2 - t1))
