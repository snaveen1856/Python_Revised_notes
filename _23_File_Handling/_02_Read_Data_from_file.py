my_file = open("C:/Users/naveen.kuruva/Desktop/sample.txt", 'r')

# Read data from file
str_1 = my_file.read()

for each in str_1.split(" "):
    if each == "appended":
        print("Appended word exists in file")

print("data to read from file ==> ", str_1)

my_file.close()
