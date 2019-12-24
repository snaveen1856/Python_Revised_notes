
import json

'''
convert python dict to json
'''
dict_1 = {
    'id': 128302,
    'name': 'Naveen kumar',
    'salary': 123947,
    'designation': 'developer'
    }

app_json = json.dumps(dict_1)
print(app_json, type(app_json))

with open('app_json', 'w') as c:
    c.write(app_json)
    c.close()
    
'''
opening json file
my = json.load(open('file name'))
'''