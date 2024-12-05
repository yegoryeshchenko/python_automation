import time

print(time.time())
print(time.localtime())

ct = time.localtime()

print(ct.tm_year)
print(ct.tm_mon)
print(ct.tm_zone)

cur_time_sec = time.time()
time.sleep(3.5)

print(f'Diff time: {time.time() - cur_time_sec}')
while time.time() - cur_time_sec < 10:
    print('Still waiting...')
    time.sleep(0.5)
