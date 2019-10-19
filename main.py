from Communication import Communication
from datetime import datetime



print('Start')
communicator = Communication()
while True:
    message = communicator.rec()
    print(message)
    # current date and time
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    print("timestamp =", timestamp)
    communicator.send("Hello")
