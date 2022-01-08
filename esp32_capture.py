import requests
import time
from datetime import datetime

interval_minutes = 5

while True:
    now = datetime.now()
    date_time = now.strftime("%Y%m%d-%H%M%S")
    print(date_time)

    response = requests.get("http://XXX.XXX.XXX.XXX/capture")

    file = open(f"{date_time}.png", "wb")
    file.write(response.content)
    file.close()

    time.sleep(60 * interval_minutes)
