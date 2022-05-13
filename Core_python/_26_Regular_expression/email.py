import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
KRam1856@gmail.com
Divyasri@gmail
'''

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
pattern = re.compile(r'[\w+-._]+@+[\w+-_.]+\.[\w]')
matches = pattern.finditer(emails)
for match in matches:
    print(match)

pattern = re.compile(r'[\w+-._]+@[\w+-_,]+\.[\w]')