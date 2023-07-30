# import time
#
# t = time.localtime()
# print(time)
# current_time = time.strftime("%H:%M:%S", t)
#
# print(current_time)

from datetime import datetime, timedelta

currentTime = datetime.now()
print(currentTime)
taskkillDateTime = currentTime + timedelta(seconds=145)
print(taskkillDateTime)
taskkillTime = f'{taskkillDateTime:%H:%M:%S}'
print(taskkillTime)