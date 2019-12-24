my_file = open("C:/Users/VNSquare Tech/Desktop/read_data.txt", 'r')

print(type(my_file))
# Read data from file
for each_line in my_file:
    if 'Python' in each_line.split():
        print(each_line)
    else:
        print("No keyword called Python in this ilne")

print("----------------------")  

# Read data from file
for each_line in my_file:
    words = each_line.split()
    print(words)
    print("----------")

# Using with statement
print("----Using with statement------")
with open("C:/Users/VNSquare Tech/Desktop/3850_3.txt", 'r') as my_file:
    for each_line in my_file:
        words = each_line.split()
        print(words)
