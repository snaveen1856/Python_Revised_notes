"""
create Node
create Linked list
add node to the linked list
print linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_Node):
        if self.head is None:
            self.head = new_Node
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = new_Node

    def printList(self):
        if self.head is None:
            print("Linked List is Empty!")
            return
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next


# creating a empty linked list
linked_list = []
# adding elements for the linked list to
linked_list.append("India")
linked_list.append("America")
linked_list.append("Canada")
linked_list.append("Switzerland")
# displaying the linked list contents
print("The linked list elements:", linked_list)
# display the operations in linked list
choice = 0
while choice < 5:
    print("Linked List Operations are")
    print("1 for Add element to linked list")
    print("2 for Remove element from linked list")
    print("3 for Replace element from linked list")
    print("4 for Search element from linked list")
    print("5 Exit")
    print("-"*40)
    choice = int(input("Enter your choice:"))
    if choice == 1:
        element = input("Enter element:")
        pos = int(input("Enter At What position:"))
        linked_list.insert(pos, element)
        print("-" * 40)
    elif choice == 2:
        try:
            element = input("Enter element:")
            linked_list.remove(element)
            print("-" * 40)
        except ValueError:
            print("Enter Element not found")
            print("-" * 40)
    elif choice == 3:
        element = input("Enter element:")
        pos = int(input("Enter position:"))
        linked_list.pop(pos)
        linked_list.insert(pos, element)
        print("-" * 40)
    elif choice == 4:
        element = input("Enter element:")
        try:
            pos = linked_list.index(element)
            print("Element found at position:", pos)
            print("-" * 40)
        except ValueError:
            print("Element not found")
            print("-" * 40)
    else:
        break
# display the linked_list
print("Linked list:", linked_list)


