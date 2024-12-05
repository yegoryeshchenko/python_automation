import time
from datetime import datetime

row1 = '2024-11-30 17:55:59'  # UTC
row2 = '24017-03T5:55:30.255 PM'  # UTC
row3 = '28-02-20 8:55:40.255 -0200'  # TZ

row1_transformed = datetime.fromisoformat(row1)
print(type(row1_transformed))

row1_transformed = datetime.strptime(row1, '%Y-%m-%d %H:%M:%S')  # returns object
row1_transformed_str = datetime.strftime(row1_transformed, '%Y/%m/%d %H:%M:%S')  # returns string
print(row1_transformed_str)
print(type(row1_transformed))
print(row1_transformed.date())

cur_time_with_tz = time.localtime()

