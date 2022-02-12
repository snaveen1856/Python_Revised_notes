import array as arr

ar = arr.array('d', [2, 3, 6, 7, 4, 8, 9])
print(ar)

# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
import array as arr
# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
# creating an array with Char/string type	
# ar1 = arr.array('u', ['navn','sai','ram','kumar'])
# print(ar1)
