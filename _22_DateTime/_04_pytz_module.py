import pytz
import datetime

print('List of all timezones:', pytz.all_timezones)
print('List of all the supported timezones:', pytz.all_timezones_set)
print('Commonly used timezones:', pytz.common_timezones)

# getting utc timezone
utc_time = pytz.UTC

# getting timezone by name
ist_time = pytz.timezone('Asia/Kolkata')

# getting datetime of specified timezone
print('Datetime of UTC Time-zone: ', datetime.datetime.now(tz=utc_time))
print('Datetime of IST Time-zone: ', datetime.datetime.now(tz=ist_time))

print('country_names =')
for key, val in pytz.country_names.items():
    print(key, '=', val, end=',')
print('\n')
print('Country name equivalent to the input country code: ', pytz.country_names['AQ'], pytz.country_timezones['AQ'])