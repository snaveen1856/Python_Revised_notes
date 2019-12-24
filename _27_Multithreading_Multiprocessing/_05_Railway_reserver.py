########   multitasking using two threads #########
from threading import *
from time import *


class Railway:  # constructor that accepts no. of available berths
    def __init__(self, available):
        self.available = available  # a method that reserves berth

    def reserve(self, wanted):  # display no. of available berths
        print('Available no. of berths=', self.available)
        # if available >= wanted, allot the berth
        if self.available >= wanted:  # find the thread name
            name = current_thread().getName()  # display berth is allotted for the person
            print('%d berths allotted for %s' % (wanted, name))  # make time delay so that the ticket is printed
            # decrease the no. of available berths
            self.available -= wanted
            sleep(1.5)

        else:  # if available < wanted, then say sorry
            print('Sorry, no berths to allot')  # create instance to Railway class
            # #specify only one berth is available


obj = Railway(1)  # create two threads and specify 1 berth is needed
t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))
# give names to the threads
t1.setName('First Person')
t2.setName('Second Person')
# run the threads
t1.start()
t2.start()
