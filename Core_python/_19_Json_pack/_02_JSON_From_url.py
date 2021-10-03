import json
from urllib.request import urlopen

with open("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR=json") as response:
    source = response.read()
    
print(source)