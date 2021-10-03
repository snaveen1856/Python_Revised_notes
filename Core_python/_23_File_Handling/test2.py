from datetime import *
import time
import pytz

n = datetime.now()
n1 = datetime.today()
curr_t = time.time()
prev_t = curr_t - 3600
while curr_t > prev_t:
    prev_t += 30
    # print(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(prev_t)))
    t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(prev_t))

    t2 = t1.replace('T', '  ')
    t2 = t1.rstrip('Z')

    datetime_tz = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
    datetime_in_utc = datetime_tz.astimezone(pytz.utc)
    date_UTC = datetime_in_utc.strftime('%Y-%m-%d %H:%M:%S %Z')
    print(date_UTC)

'''print('i1=',i1)   
print('i=',i)
print('n=',n)
print('n1=',n1)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i1)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i))) '''
