my_file = open("C:/Users/VNSquare Tech/Desktop/read_data.txt", 'r')

# Read data from file
str = my_file.read()

for each in str.split(" "):
        if each == "appended":
            print("Appended word exists in file")

print("data to read from file ==> ",str)

my_file.close()
