import datetime
import pytz

d = datetime.datetime(2020, 3, 20, 14, 45, 50)
utc = pytz.UTC
pst = pytz.timezone('America/New_York')
da = utc.localize(d)
print(da)
s = d - datetime.timedelta(days=23)
print(s)

