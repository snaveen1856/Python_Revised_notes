import re

string0 = "The rain in Spain"
x = re.search("in", string0)
print(x)

string1 = "The rain in Spain"
x = re.split("\s", string1)
print(x)
