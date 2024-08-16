import time
from datetime import datetime

current_time = time.time()
today = datetime.today()
print("Seconds since January 1, 1970: " +
      f'{current_time:,.4f} or {current_time:e} in scientific notation')
print(f'{today:%b %d %Y}')
