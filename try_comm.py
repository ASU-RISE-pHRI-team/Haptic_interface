# import zmq
#
# context = zmq.Context()
# socket_in1 = context.socket(zmq.SUB)
# socket_in1.connect("tcp://10.203.53.193:9001")
# topic_filter = b""
# socket_in1.setsockopt(zmq.SUBSCRIBE, topic_filter)
# while True:
#     val = socket_in1.recv_string()
#     print(val)


import time

k = time.time()
m = 0
while m < 5:
    t1 = time.time()
    t2 = time.time()
    m = int(t2 - k)
    print(t2)

    if t2-t1-0.5 < 0:
        time.sleep(0.5 + t1 - t2)
