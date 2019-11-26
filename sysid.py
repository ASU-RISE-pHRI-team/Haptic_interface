import threading
import zmq
import json
import numpy as np
import time
from optimal_agent import Optimalagent
from parameters import Parameters1
from communication import Communication
import csv


def main():
    global agent
    try:
        agent = Optimalagent(Parameters1)
        kim = Communication()
        kim.run()
        kim.runner1()
        kim.runner2()
        time.sleep(3)
        print(kim.state)
        state_set = [kim.state]
        action_1 = 0
        action_2 = 0
 
        while True:
            t1 = time.time()
            kim.translate()
            agent.state = kim.state

            print(agent.state)
            msg1 = {"force_x": action_1, "force_y": 0, "force_z": 0}
            msg2 = {"force_x": action_2, "force_y": 0, "force_z": 0}
            #msg1 = {"force_x": 0, "force_y": 0, "force_z": 0}
            #msg2 = {"force_x": 0, "force_y": 0, "force_z": 0}
            msg1_json = json.dumps(msg1)
            msg2_json = json.dumps(msg2)  # pallavi
            kim.send(msg1_json)
            kim.my_sender(msg2_json)  # pallavi

            t2 = time.time()
            agent.data_append(kim.state, action_1)
            if t2 - t1 - Parameters1.T < 0:
                time.sleep(Parameters1.T - t2 + t1)
    except KeyboardInterrupt:

        np.savetxt("trans_zero.csv", agent.state_set, delimiter=",")


if __name__ == '__main__':
    main()
