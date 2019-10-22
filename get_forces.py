import zmq


class Communication:

    def __init__(self):
        context = zmq.Context()
        self.socket_in = context.socket(zmq.SUB)
        self.socket_out = context.socket(zmq.PUB)
        self.socket_in.connect("tcp://localhost:5577")
        self.socket_out.bind("tcp://*:5578")

    def rec(self):
        topic_filter = b""
        self.socket_in.setsockopt(zmq.SUBSCRIBE, topic_filter)
        msg = self.socket_in.recv_string()
        return msg

    def send(self, data):
        #  Send reply back to client
        self.socket_out.send_string(data)
