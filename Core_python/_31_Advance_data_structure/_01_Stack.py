"""
Stack in Python:
===============
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
In stack, a new element is added at one end and an element is removed from that end only. The insert and delete
operations are often called push and pop.

Method of Stack :
=================
empty() – Returns whether the stack is empty – Time Complexity : O(1)
size() – Returns the size of the stack – Time Complexity : O(1)
top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
pop() – Deletes the top most element of the stack – Time Complexity : O(1)
Implementation
"""


class Stack:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def push(self, val):
        if val:
            self.stack.append(val)
        else:
            print("Enter a proper value")

    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.stack.pop()

    def peep(self):
        n = len(self.stack)
        return self.stack[n-1]

    def search(self, item):
        if self.isempty():
            return -1
        else:
            try:
                # print("we are in search method Try block", dir(self.stack))
                n = self.stack.index(item)
                print("we are in search method Try block", n)
                f = len(self.stack)-n
                return n
            except ValueError:
                return -2

    def __str__(self):
        return f"The Stack: {self.stack}"


stack = Stack()
choice = 0
# display Stack Operations
while choice < 5:
    print("Stack operations")
    print("1.To Push element to stack")
    print("2.To Pop element from stack")
    print("3.To Peep element from stack")
    print("4.To Search element from stack")
    print("5.To exit")
    print("-"*40)
    choice = int(input("Enter any one option from above:"))
    if choice == 1:
        element = input("Enter an element to push:")
        stack.push(element)
        print("Stack is now:", stack)
        print("-" * 40)
    elif choice == 2:
        element = stack.pop()
        if element == -1:
            print("Stack is empty")
            print("-" * 40)
        else:
            print("Popped element:", element)
            print("Stack is now:", stack)
            print("-" * 40)
    elif choice == 3:
        element = stack.peep()
        print("Topmost element:", element)
        print("-" * 40)
    elif choice == 4:
        element = int(input("Enter element to search:"))
        pos = stack.search(element)
        print("position:", pos)
        if pos == -1:
            print("The Stack is empty")
            print("-" * 40)
        elif pos == -2:
            print("Element not found in the Stack")
            print("-" * 40)
        else:
            print("Element found at position:", pos)
            print("-" * 40)
    else:
        print(stack)
        break
