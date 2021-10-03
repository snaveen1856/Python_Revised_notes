def line_word_count(fname, separator):
    with open(fname) as f:
        data = f.readlines()
        lcount = 0
        wcount = 0
        for row in data:
            feilds = row.split(separator)
            wcount += len(feilds)
            lcount += 1
    return lcount, wcount


fname = input('Enter file name: ')
separator = input('Enter separator: ')
lcount, wcount = line_word_count(fname, separator)
print('Lines: ', lcount)
print('Words: ', wcount)

print('-' * 50)
with open('student.txt') as f:
    data1 = f.read(5)
    data2 = f.read()
print(data1)
print(data2)
