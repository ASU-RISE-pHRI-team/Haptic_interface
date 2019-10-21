from communication_new import Communication
from datetime import datetime
from optimal_agent import Optimalagent
import time
print('Start')
communicator = Communication()
#controller = Optimalagent()
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

    t2 = time.time()
    if t2-t1 > 0:
        #print(T - (t2-t1))
        time.sleep(T - (t2-t1))
