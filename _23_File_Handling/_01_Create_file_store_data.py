fname = input('Enter a new file name:')
my_file = open(fname, 'w')

data = input("Enter text : ")

my_file.write(data)

my_file.close()
print("---Completed")
