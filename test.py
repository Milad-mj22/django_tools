from datetime import datetime
from time import sleep


while True:
     now=datetime.now()
     current_time=now.strftime("%H:%M:%S")
     time=print("Current Time : ", current_time)
     sleep(1)