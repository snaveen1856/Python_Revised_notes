import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
http://10.10.1.12:8000
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
subbed_urls = pattern.sub(r'\2\3', urls)
print('======== using sub string =======')
print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))
