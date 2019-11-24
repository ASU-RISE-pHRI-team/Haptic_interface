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
        action_1 = -1.0
        action_2 = 1.0

        while True:
            t1 = time.time()
            kim.translate()
            agent.state = kim.state

            print(agent.state)
            msg1 = {"force_x": action_1, "force_y": 0, "force_z": 0}
            msg2 = {"force_x": action_2, "force_y": 0, "force_z": 0}
            msg1_json = json.dumps(msg1)
            msg2_json = json.dumps(msg2)  # pallavi
            kim.my_sender(msg2_json)  # pallavi
            kim.send(msg1_json)
            t2 = time.time()
            agent.data_append(kim.state, action_1)
            if t2 - t1 - Parameters1.T < 0:
                time.sleep(Parameters1.T - t2 + t1)
    except KeyboardInterrupt:
        # with open("my_data.csv", mode="w") as f:
        #     writer = csv.writer(f, delimiter=',')
        #     writer.writerows(agent.state_set[0, :])
        #     writer.writerows(agent.state_set[1, :])
        #     writer.writerows(agent.state_set[2, :])
        #     writer.writerows(agent.state_set[3, :])
        #     writer.writerows(agent.state_set[4, :])
        #     writer.writerows(agent.state_set[5, :])

        np.savetxt("rotation1.csv", agent.state_set, delimiter=",")


if __name__ == '__main__':
    main()