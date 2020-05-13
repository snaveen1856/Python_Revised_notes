"""
Queue in Python:
===============
Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue
the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where
the consumer that came first is served first.

Methods of Queue:
================
Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed.
        If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
Front: Get the front item from queue – Time Complexity : O(1)
Rear: Get the last item from queue – Time Complexity : O(1)

"""


class Queue:
    def __init__(self):
        self.queue = []
        # self.rev_list = []

    def enqueue(self, val):
        if val:
            self.queue.append(val)
        else:
            print("Entered value is not appendable!")

    def dequeue(self):
        self.queue.reverse()
        self.queue.pop()
        self.queue.reverse()

    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[len(self.queue) - 1]

    def __str__(self):
        return f"The Queue is: {self.queue}"


"""
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q)
print(q.front())
print(q.rear())
"""

a = Queue()
while True:
    print("1.To Enqueue item to Queue")
    print("2.To Dequeue item from Queue")
    print("3.To exit")
    inp = int(input("Enter any one option from above:"))
    if inp == 1:
        item_inp = input("enter an item to add in queue:")
        a.enqueue(item_inp)
    elif inp == 2:
        a.dequeue()
    else:
        print(a)
        exit()
