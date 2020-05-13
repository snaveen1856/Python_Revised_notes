file_name = 'C:\\Users\\naveen.kuruva\\Desktop\\sample.txt'
"""
with open(file_name, 'r') as f:
    line = f.read()
    line.split(",")
    print(line.split(","))
    total = sum([int(num) for num in line.split(',')])
    print(total) 
    """

new_list = []
with open(file_name, 'r') as fr:
    line_data = fr.readline()
    print('lines in file:', line_data)
    for row in line_data:
        row = row.rstrip('\n')
        list_words = row.split(' ')
        # list_words1 = row.split(',')
        # list_words.extend(list_words1)
        # print('words in a list:', list_words)
        for num in list_words:
            if num.isnumeric():
                new_list.append(num)
print(new_list)
sum_num = 0
for i in new_list:
    i = int(i)
    sum_num += i
print(sum_num)
