"""
import threading

print('let us find the current thread:')
print('The current thread is:', threading.current_thread().getName())
if threading.current_thread() == threading.main_thread():
    print('Current thread is the main thread')
else:
    print('The current is not the main thread')
"""
"""
 Creating a thread without using a class  
 Creating a thread by creating a sub class to Thread class 
 Creating a thread without creating sub class to Thread class  Creating a Thread without using
 """
""" 
#########  creating a thread without using a class ################
from threading import *


# create a function
def display():
    print('Hello I am running')
    # create a thread and run the function for 5 times


for i in range(5):  # create the thread and specify the function as its target
    t = Thread(target=display)
    # run the thread
    t.start()
"""
"""
############ creating our own thread #############
from threading import Thread


# create a class as sub class to Thread class
class MyThread(Thread):
    # override the run() method of Thread class
    def run(self):
        for i in range(1, 6):
            print(i)
        # create an instance of MyThread class


t1 = MyThread()
# start running the thread t1
t1.start()  # wait till the thread completes execution
t1.join()
"""
"""
######## a thread that accesses the instance variables ##########
from threading import *


# create a class as sub class to Thread class
class MyThread(Thread):
    # constructor that calls Thread class constructor
    def __init__(self, str_1):
        Thread.__init__(self)
        self.str_1 = str_1
        # override the run() method of Thread class

    def run(self):
        print(self.str_1)
        # create an instance of MyThread class and pass the string


t1 = MyThread('Hello')
# start running the thread t1
t1.start()  # wait till the thread completes execution
t1.join()
"""
# creating a thread without making sub class to Thread class
from threading import *


# create our own class
class MyThread:
    # a constructor
    def __init__(self, str_):
        self.str_ = str_
        # a method

    def display(self, x, y):
        print(self.str_)
        print('The args are:', x, y)

    # create an instance to our class and store ‘Hello’ string


obj = MyThread('Hello')  # create a thread to run display method of obj
t1 = Thread(target=obj.display, args=(1, 2))
# run the thread
t1.start()
