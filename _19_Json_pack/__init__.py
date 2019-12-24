import json
import os
'''
convert python dict to json
'''
dict1 ={'Students':[ {'id': 128302,
                     'name': 'Naveen',
                    'salary': 123947,
                    'designation': 'Python Developer'},
                   {'id': 128300,
                     'name': 'Naveen Kumar',
                    'salary': 120000,
                    'designation': 'Java Developer'},
                  {'id': 128303,
                     'name': 'Sai',
                    'salary': 123000,
                    'designation': 'Python Developer'} ]
                     
         }                               
#list1 = [100,25000,'Naveen',5000]
#app_json1 = json.dumps(list1) 
app_json = json.dumps(dict1)
print(app_json)
print(type(app_json))

with open('app_json', 'w') as c:
    c.write(app_json)
    #c.write(app_json1)
    print(type(c))  
    c.close()
print('-----------------------------------------------')    
print(app_json.split(':'))
s=app_json.split(':')
for i in app_json.split(':'):
   print(i)
     
        
'''
opening json file.
my = json.load(open('file name'))
'''