from Node import *
#Single Linked List class
class singlelinkedlist:
   
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
        elif pos == 0:
            node.next = self.head
            self.head = node
        elif pos == None:
            node.next = None
            self.tail.next = node
            self.tail = node
        else:
            current = self.head
            for _ in range(pos-1):
                if current is self.tail :
                    break
                current = current.next

            if current is self.tail:
                print("This position is invalid so adding value at the end of list")
                self.tail = node
            node.next = current.next
            current.next = node
                
            

    #Adding an iterable to list
    def extend(self,list,pos=None):
        for x in list:
            self.addnode(x,pos)
            if pos != None:
                pos+=1

    #Printing list
    def printlist(self):
        if self.head is self.tail and self.head == None:
            print("List is Empty",end="\n")
        else:
            current = self.head
            while current is not self.tail:
                print(current.value,end = " ")
                current  = current.next
            print(current.value)
        
    #Removing nodes based on value
    def remove_value(self,search):
        if self.head == self.tail:
            if self.head ==None:
                print("List is already empty")
            elif self.head.value == search:
                self.head = None
                self.tail = None
            else:
                print("Element is not in list")
        else:
            current = self.head
            while current.value != search and current is not self.tail:
                
                previous = current
                current = current.next
            if current.value == search:
                if current is self.tail:
                    self.tail = previous
                    previous.next = None
                elif current is self.head:
                    self.head = current.next
                    current.next = None
                else:
                    previous.next = current.next
                    current.next = None
            else:
                print("Element not found")

    #Removing nodes based on position
    def remove_pos(self,pos=None):
        if self.head == self.tail:
            if self.head == None:
                print("List is already empty")
            else:
                self.head = None
                self.tail = None
        elif pos == 0:
            self.head = self.head.next
        elif pos == None:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            self.tail = current
            current.next = None
        else:
            current = self.head
            for _ in range(pos-1):
                if current.next is self.tail:
                    break
                current = current.next
            if current.next is self.tail:
                print("Invalid position so removing last node")
                current.next = None
                self.tail = current
            else:
                current.next = current.next.next

                        
    def deletelist(self):
        self.head = None
        self.tail = None


