"""
filename = input('Enter a file name:')
filename = 'C:\\Users\\Ram.kuruva\\Desktop\\emp.txt'
with open(filename, 'r') as f:
    line = f.read()
    # print(line)
    line_count = line.rsplit('\n')
    print("this will count line:", line_count)
    line_data = line.split(' ')
    num = []
    print(line_data)
    count_l = 0
    for _ in line_data:
        count_l += 1
    print(f'Word count in the file is:{count_l}')
    for n in line_data:
        if n.isdigit():
            n = int(n)
            num.append(n)
    print(num)
    print(sum(num))
"""
import re

urls = """ https://www.google.com 
           http://coreyms.com
           https://youtube.com
           https://nasa.com
           http://homedepot.com
           http://ikya.in 
      """
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
subbed_urls = pattern.sub(r'\2\3', urls)
print("-"*50)
print(subbed_urls)
