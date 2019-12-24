import time
from calendar import month

# EPOCH Time
epoch = time.time()
print("Epoch  Time :", epoch)

# Current Time
current_time = time.ctime()
print("Current time      :", current_time)

# Current Date Time
from datetime import *

now = datetime.now()
print("Current Date time :", now)
print("Date now          : {}-{}-{}".format(now.day, now.month, now.year))

# Today's date and Time

tdm = datetime.today()
print("Today's Date & Time :", tdm)

td = date.today()
print("Today's Date        :", td)
print("Today's Date      :", td.strftime("%d, %B, %Y"))

# CALENDAR
import calendar
from calendar import month

yy = int(input("Enter year : "))
mm = int(input("Enter month: "))

str1 = month(yy, mm)
print("Calendar for Current Month", str1)

year = int(input("Enter year :"))
print(calendar.calendar(year, 2, 1, 8, 3))
