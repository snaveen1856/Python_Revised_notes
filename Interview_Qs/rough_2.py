"""
for i in range(len(data_list)):
    for j in range(i + 1, len(data_list)):

        if data_list[i] > data_list[j]:
            data_list[i], data_list[j] = data_list[j], data_list[i]

print(data_list)"""

"""
l = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]
print(l)
for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
            # print(l[i], l[j])
            l[i], l[j] = l[j], l[i]
            # print(l[i], l[j])
print(l)            

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
"""
