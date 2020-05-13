# 1. Parse date strings
"""
import datetime
import pytz
import dateutil.parser

format = '%Y-%m-%dT%H:%M:%S%z'
datestring = '2020-03-20T16:43:45-07:00'
d = dateutil.parser.parse(datestring)
da = datetime.datetime.strptime(datestring, format)
print("d:", d)
print('da:', da)
"""
# 2. ISO-8601 date string to UTC datetime object
import datetime
import pytz
import dateutil.parser

utc = pytz.UTC
format = '%Y-%m-%dT%H:%M:%S%Z'
datestring = '2020-09-01T16:43:45-07:00'
d = dateutil.parser.parse(datestring)
da = d.replace(tzinfo=utc) - d.utcoffset()
daf = datetime.datetime(2020, 3, 20, 14, 45, 50, tzinfo=utc)
print(d)
print(daf)
