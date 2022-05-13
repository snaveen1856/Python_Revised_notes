import sys
import os
import json


def Output(file):
    # json format file how to convert txt to json
    # json data get into python
    # convert to ditionary
    # iterate
    print("iin output")
    f = open(file, "r")
    lines_data = f.readlines()
    # print(lines_data)
    d = {}
    if 'Syslab' in lines_data:
        print('hi')


'''
for each in lines_data:
if 'SysLab' in fa
print(each)
 print(dict)
'''


def getfile(filename):
    data = {
        "arr.txt": "/home/nityaobject/Desktop/prasanna/posttxt/arr.txt",
        "arrayspace.txt": "/home/nityaobject/Desktop/prasanna/posttxt/arrayspace.txt",
        "authen.txt": "/home/nityaobject/Desktop/prasanna/posttxt/authen.txt",
        "creses.txt": "/home/nityaobject/Desktop/prasanna/posttxt/creses.txt",
        "drive.txt": "/home/nityaobject/Desktop/prasanna/posttxt/drive.txt",
        "hgroup.txt": "/home/nityaobject/Desktop/prasanna/posttxt/hgroup.txt",
        "hgroupspace.txt": "/home/nityaobject/Desktop/prasanna/posttxt/hgroupspace.txt",
        "host.txt": "/home/nityaobject/Desktop/prasanna/posttxt/host.txt",
        "hspace.txt": "/home/nityaobject/Desktop/prasanna/posttxt/hspace.txt",
        "monitor.txt": "/home/nityaobject/Desktop/prasanna/posttxt/monitor.txt",
        "pgroup.txt": "/home/nityaobject/Desktop/prasanna/posttxt/pgroup.txt",
        "port.txt": "/home/nityaobject/Desktop/prasanna/posttxt/port.txt",
        "ver.txt": "/home/nityaobject/Desktop/prasanna/posttxt/ver.txt",
        "volume.txt": "/home/nityaobject/Desktop/prasanna/posttxt/volume.txt",
        "volumespace.txt": "C:/Users/Ram Karna/Desktop/volumespace.txt",

    }

    if filename in data.keys():
        return Output(data.get(filename))

    else:
        print("give proper file name")


if __name__ == "__main__":
    print('ram')
    filename = sys.argv[1]
    print(filename)
    find = sys.argv[2]
    print('sam')
    print(find)
    data = getfile(filename)
    jsondata = json.dumps(data)

    for i in jsondata:
        if find == i:
            print(i)
