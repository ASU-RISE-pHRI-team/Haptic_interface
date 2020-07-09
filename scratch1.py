import zmq
import json

context5 = zmq.Context()
print("1")
socket_in3 = context5.socket(zmq.SUB)
print("2")
socket_in3.connect("tcp://192.168.1.2:1501")
print("3")
topic_filter = b""
print("4")
socket_in3.setsockopt(zmq.SUBSCRIBE, topic_filter)
print("5")
while True:
    print("start import")
    other_forces = socket_in3.recv_string()
    print("importing")
    other_forces = json.loads(other_forces)
    print(other_forces)
