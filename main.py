import get_forces
from datetime import datetime
from optimal_agent import Optimalagent
import time
import get_location

print('Start')
communicator_1 = get_location.Communication()
communicator_2 = get_forces.Communication()
# controller = Optimalagent()
T = 0.05
while True:
    t1 = time.time()
    message_1 = communicator_1.rec()
    message_2 = communicator_2.rec()
    print(message_1)
    print(message_2)
    # current date and time
    now = datetime.now().isoformat(timespec='microseconds')
    print("timestamp =", now)
    # timestamp = datetime.timestamp(now)
    # print("timestamp =", timestamp)
    communicator_1.send(message_1)
    communicator_2.send(message_2)

    pos, rot, vel, r_vel = communicator_1.translate()
    print("Position of the block =", pos)
    print("Velocity of the block =", vel)
    print("Angular position of the block =", rot)
    print("Angular velocity of the block =", r_vel)

    t2 = time.time()

    # if t2 - t1 > 0:
    #     print(T - (t2 - t1))
    #     time.sleep(T - (t2 - t1))
