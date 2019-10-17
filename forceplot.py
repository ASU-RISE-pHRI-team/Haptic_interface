import time
import zmq
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
mymat=np.zeros([4, 101])
k = 0
context = zmq.Context()
socket_in = context.socket(zmq.SUB)
socket_out = context.socket(zmq.PUB)
socket_in.connect("tcp://localhost:5577")
socket_out.bind("tcp://*:5578")
topicfilter = b""
socket_in.setsockopt(zmq.SUBSCRIBE, topicfilter)
#while True:
while k <= 100:
    print("/n")
    #  Wait for next request from client
    message = socket_in.recv_string()
    #print("Received request: %s" % message)
    print(message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket_out.send(b"World")
    #print ("Hello")
    jmsg = json.loads(message)
    jp=jmsg["Position"]
    jf=jmsg["Force"]
    #print(jp)
    print(jf)
    mymat[0, k] = jp[0]
    mymat[1, k] = jp[1]
    mymat[2, k] = jp[2]
    mymat[3, k] = jf[0]
    k = k+1
    print(k)

print(mymat)

with open('my_data.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        data_writer.writerow(mymat[0, :])
        data_writer.writerow(mymat[1, :])
        data_writer.writerow(mymat[2, :])
        data_writer.writerow(mymat[3, :])

plt.figure()
plt.subplot(311)
plt.plot(mymat[0, :], mymat[3, :])
plt.show()


plt.subplot(312)
plt.plot(mymat[1, :], mymat[3, :])
plt.show()


plt.subplot(313)
plt.plot(mymat[2, :], mymat[3, :])
plt.show()

#with open('mydata.csv', mode='w') as data_file:
 #       data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
 #       data_writer.writerow([jp])
  #      data_writer.writerow([jf])
