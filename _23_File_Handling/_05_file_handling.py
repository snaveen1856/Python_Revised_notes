# PROGRAM TO READ AND WRITE  DATA FROM A FILE

in_data = open("C:/Users/VNSquare Tech/Desktop/names.txt", "w")
in_data.write("Welcome to the world of Python")
print("---After writing to file DATA : ", in_data)
in_data.close()

out_data = open("C:/Users/VNSquare Tech/Desktop/names.txt", "r")
out_data = out_data.read()
print("---Reading from file  : ", out_data)
# out_data.close()

obj2 = open("C:/Users/VNSquare Tech/Desktop/names.txt", "r")
text_data = obj2.read(15)
print("---Reading from file  with byte size : ", text_data)
obj2.close()
