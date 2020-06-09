from Node import *
#Circular Linked List Class    
class CircularLinkedList:
    #Defining Linkedlist
    def __init__(self):
        self.head = None
        self.tail = None
    #Adding Nodes to positions
    def addnode(self,value,pos=None):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            node.next = self.head
        elif pos == 0:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        elif pos == None:
            node.next = self.head
            self.tail.next = node
            self.tail = node
        else:
            current = self.head
            for _ in range(pos-1):
                if current is self.tail:
                    break
                current = current.next
            if current is self.tail:
                print("This position is invalid so adding value at the end of list")
                self.tail = node
            node.next = current.next
            current.next = node
            

    #Printing list
    def printlist(self):
        current = self.head
        while current is not self.tail:
            print(current.value)
            current  = current.next
        print(current.value)