sentence = 'This is a sentence'
split_value = []
tmp = ''
for c in sentence:
    # print(tmp)
    # print(c)
    if c == ' ':
        # print(tmp)
        split_value.append(tmp)
        # print(split_value)
        tmp = ''
    else:
        tmp += c
if tmp:
    split_value.append(tmp)
print(split_value)
string = ''
space = " "
for word in split_value:
    string += space + word
print(string)
