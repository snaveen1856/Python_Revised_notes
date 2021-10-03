# PROGRAM TO READ AND WRITE  DATA FROM A FILE

in_data = open("C:/Users/naveen.kuruva/Desktop/sample1.txt", "w")
in_data.write("Welcome to the world of Python")
print("---After writing to file DATA : ", in_data)
in_data.close()

out_data = open("C:/Users/naveen.kuruva/Desktop/sample1.txt", "r")
out_data = out_data.read()
print("---Reading from file  : ", out_data)
# out_data.close()

obj2 = open("C:/Users/naveen.kuruva/Desktop/sample1.txt", "r")
text_data = obj2.read(15)
print("---Reading from file  with byte size : ", text_data)
obj2.close()
