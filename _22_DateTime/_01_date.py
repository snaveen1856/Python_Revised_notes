"""
from datetime import datetime
import pytz

# METHOD 1: Hardcode zones:
from_zone = pytz.gettz('UTC')
to_zone = pytz.gettz('America/New_York')

# METHOD 2: Auto-detect zones:
from_zone = pytz.tzutc()
to_zone = pytz.tzlocal()

# utc = datetime.utcnow()
utc = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')

# Tell the datetime object that it's in UTC time zone since
# datetime objects are 'native' by default
utc = utc.replace(tzinfo=from_zone)

# Convert time zone
central = utc.astimezone(to_zone)
"""
import pytz
import datetime as dt

n = dt.date(2019, 9, 1)
print(n)
local_tz = pytz.timezone("Asia/Hong_Kong")
datetime_without_tz = dt.datetime.strptime("2019-09-25T08:32:05Z", "%Y-%m-%dT%H:%M:%SZ")
datetime_with_tz = local_tz.localize(datetime_without_tz, is_dst=None)  # No daylight saving time
datetime_in_utc = datetime_with_tz.astimezone(pytz.utc)

str1 = datetime_without_tz.strftime('%Y-%m-%d %H:%M:%S %Z')
str2 = datetime_with_tz.strftime('%Y-%m-%d %H:%M:%S %Z')
str3 = datetime_in_utc.strftime('%Y-%m-%d %H:%M:%S %Z')

print('Without Timzone : %s' % (str1))
print('With Timezone   : %s' % (str2))
print('UTC Datetime    : %s' % (str3))
