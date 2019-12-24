s = 'Hello world'

n = "Hi! Madam, how are you doing?"

k = '''Hi! Sindhu, 
How are you? I'm waiting here
Come to my home.'''

print(s)
print('\n', n)
print('\n', k)
print('-----------Concadinating all string-------------')
print('\n', s, '\t' + n, '\t' + k)
print('---------Replications of all string--------------')
print('\n', s * 3)
print('\n', n * 2)
print('--------Slice operation-----------')
print(s[1:5:1])
print(s[0:6])
print(s[::-1])
print(s[::2])
print(s[0:8:3])
n = 'madam'
print('Reversing the String Madam: ', n[::-1])
