import time
import zmq

context = zmq.Context()
socket_in = context.socket(zmq.SUB)
socket_out = context.socket(zmq.PUB)
socket_in.connect("tcp://localhost:5577")
socket_out.bind("tcp://*:5578")
topicfilter = b""
socket_in.setsockopt(zmq.SUBSCRIBE, topicfilter)
#while True:
while True:
    #  Wait for next request from client
    print("Start")
    message = socket_in.recv_string()
    #print("Received request: %s" % message)
    print(message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket_out.send(b"World")




