my_file = open("sample.txt", 'r')

print(type(my_file))
# Read data from file
for each_line in my_file:
    print(each_line)
    # if 'Python' in each_line.split():
    #     print(each_line)
    # else:
    #     print("No keyword called Python in this line")

print("------------------------------------------------------------------------------------------------------")

# Read data from file
for each_line in my_file:
    words = each_line.split(" ")
    print(words)
print("----------------------------------------------------------------------------------------------------")

# Using with statement
print("----------------Using with statement----------------------")
with open("sample.txt", 'r') as my_file:
    for each_line in my_file:
        words = each_line.split()
        print(words)
