import os
import json
import datetime
import pytz
import sys
import time


def Output(file):
    f = open(file, "r")
    return f.readlines()


def getfile(filename):
    data = {
        "volume.txt": "/home/nityaobject/Desktop/prasanna/posttxt/volume.txt",
        "volumespace.txt": "C:/Users/manne/Documents/test.txt"

    }

    if filename in data.keys():
        return Output(data.get(filename))

    else:
        print("give proper file name")


if __name__ == "__main__":
    # filename= sys.argv[1]
    filename = 'test.txt'
    # fi = sys.argv[2]
    # print(fi)
    str1 = " "
    data = getfile(filename)
    print(data)
    jsondata = json.loads(str1.join(data))

    for i in jsondata:
        time.sleep(30)
        # print(i)
        # print(i.keys())
        if "time" in i.keys():
            t_val = i.get("time")
            t1 = t_val.replace('T', ' ')
            t1 = t1.rstrip('Z')
            datetime_tz = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
            datetime_in_utc = datetime_tz.astimezone(pytz.utc)
            date_UTC = datetime_in_utc.strftime('%Y-%m-%d %H:%M:%S %Z')

            print(date_UTC)
            # print(t_val)
