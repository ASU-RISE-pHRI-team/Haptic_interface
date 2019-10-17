import zmq


class Communication:
    @staticmethod
    def rec():
        context = zmq.Context()
        socket_in = context.socket(zmq.SUB)
        # socket_out = context.socket(zmq.PUB)
        socket_in.connect("tcp://localhost:5577")
        # socket_out.bind("tcp://*:5578")
        topic_filter = b""
        socket_in.setsockopt(zmq.SUBSCRIBE, topic_filter)
        msg = socket_in.recv_string()
        return msg

    @staticmethod
    def send(data):
        context = zmq.Context()
        socket_out = context.socket(zmq.PUB)
        socket_out.bind("tcp://*:5578")
        #  Send reply back to client
        socket_out.send_string(data)


######### For calling the functions from the classes ################
while True:
    #  Wait for next request from client
    # print("Start")
    message = Communication.rec()
    print(message)
    Communication.send("Hello")
