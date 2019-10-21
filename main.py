from communication_new import Communication
from datetime import datetime
from optimal_agent import Optimalagent
import json
import time
import math as m
import numpy as np

print('Start')
communicator = Communication()
# controller = Optimalagent()
T = 0.05
while True:
    t1 = time.time()
    message = communicator.rec()
    print(message)
    # current date and time
    now = datetime.now().isoformat(timespec='microseconds')
    print("timestamp =", now)
    # timestamp = datetime.timestamp(now)
    # print("timestamp =", timestamp)
    communicator.send(message)
    # jmsg = json.loads(message)
    # jr = jmsg["Rotation"]
    # theta = jr[1]
    # p = np.array([m.cos(theta), 0, m.sin(theta)])
    # jw = jmsg["Angularvelocity"]
    # jv = jmsg["Velocity"]
    # r = np.array(jr)
    # w = np.array(jw)
    # v = np.array(jv)
    # v_req = v - np.cross(p, w)
    v_req = communicator.translate()
    print("Velocity of block =", v_req)
    t2 = time.time()
    # if t2 - t1 > 0:
    #     print(T - (t2-t1))
    #     time.sleep(T - (t2 - t1))
