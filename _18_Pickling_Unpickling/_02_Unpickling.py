import pickle

pickle_off = open("C:/Users/naveen.kuruva/_1856_Python_All_programs/_18_Pickling_Unpickling/datafile1.txt", "rb")
emp = pickle.load(pickle_off)
for i in emp:
    print(i)
    # if i[3]>=50000:
    # print('Bonus:',i[3]*1.5)
print(type(emp))
print(emp)
