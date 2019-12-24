'''

@author: mnettem
'''
from sys import getsizeof

message1 = 'hello world!'
print("----message1-----",message1)

message2 = "PYTHON PROGRAMMING!"
print("----message2-----",message2)

'''
1. indexing
2. slicing
3. adding
4. multiplying and
5. checking for membership.
'''

# 1 INDEXING
print("----- 1st index in message1 -----",message1[4])
print("----- 4th index in message1 -----  Positive : ",message1[1],"  Negative :  ", message1[-11])

# 2 SLICING 
print("Slicing positive : ",message1[6:11])  # print from index 6 to position 11
print("Slicing Negative : ",message1[-6:-1]) #
print("Slicing with start stop step : ",message2[0:13:1], " == ",message2[0:13], "  ",message2[0:13:2]," ",message2[0:13:3])
print("Slicing without any positions + :",message2[::],"  ",message2[2::]," ",message2[:8:]," ",message2[::2]," ",message2[::3])
print("Slicing without any positions - :",message2[::],"  ",message2[-2::]," ",message2[:-8:]," ",message2[::-2]," ",message2[::-3])



# 3 ADDING CONCATINATION

final_message = message1 + " Welcome to " + message2 

print("Concatenation :: ",final_message)



# 4 MULTIPLYING
print("Multiplication : ", message1*4)
print("Multiplication : ", final_message*4)


# 5 CHECKING FOR MEMBERSHIP
print("--Membership---- : ", "PYTHON" in message2)


#BUILT IN STRING METHODS
print("---Capitalize -- ",message1.capitalize()) # Capitalizes first letter of string
print("---Count-------- ",message2.count('O'),"  ",message2.count('O',6,15)) #start,end are optional

#String Formatting Operators
print("My name is %s and weight is %d kg!" % ('Zara', 21))

#ASCII  Unicode
str1 = "Madhu"
str2 = u"Madhu"
print(str1,"  ",len(str1),"  ",len(str2))
print(getsizeof(str1)," ",getsizeof(str2))
