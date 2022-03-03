with open('test.txt', '+w') as fdata:
    string = 'Hello world'
    fdata.write(string)


str1 = input('enter first string:')
str2 = input('enter second string:')

chr_list = [j for i in str1 for j in str2 if j == i]
print(chr_list)

# django-admin starproject <name>
# MVT
