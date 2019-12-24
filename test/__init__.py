dict1 = {"ten":"a","two":"b","one":"a","three":"b"}

'''
{"a":["ten","one"]."b":["two","three"]}
from test.test_heapq import SideEffectLT
'''
dict2 = {}
for key,val in dict1.items():
    if val not in dict2.keys():
        dict2[val] = []
        dict2[val].append(key)
    else:
        dict2[val].append(key)
        
print(dict2)

# construcotor method 


class Student:
    
    def __init__(self,sid,name,section):
        self.sid = sid 
        self.name = name
        self.section = section 
        
    def student_details(self):
        print("Student details are :")
        print(self.sid," ",self.name," ",self.section)
        
        
naveen = Student(100,"NaveenKumar K","S1")

naveen.student_details()


list1 = [1,2,3,4,5,6,7,8,9,10,12,52,51,45,8,14]
list2 = list(filter(lambda x: (x%2 == 0), list1))
print(list2)
