import time
import zmq

context = zmq.Context()
socket_in = context.socket(zmq.SUB)
socket_out= context.socket(zmq.PUB)
socket_in.bind("tcp://*:5577")
socket_out.bind("tcp://localhost:5578")


while True:
    #  Wait for next request from client
    message = socket_in.recv()
    # print("Received request: %s" % message)
    print(message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket_out.send(b"World")