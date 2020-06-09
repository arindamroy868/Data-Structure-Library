from Node import *
#Double Linked List
class doublelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    #Adding Nodes
    def addnode(self,value,pos=None):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        elif pos == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif pos == None:
            node.prev = self.tail
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
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                node.next = current.next
                current.next.prev = node
                node.prev = current
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
        
    #Removing nodes from list
    def remove(self,search):
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
                    current.prev = None
                    previous.next = None
                    self.tail = previous
                elif current is self.head:
                    self.head = current.next
                    self.head.prev = None
                    current.next = None
                else:
                    previous.next = current.next
                    current.next = None
                    current.next.prev = previous
                    current.next = None
            else:
                print("Element not found")

    def deletelist(self):
        self.head = None
        self.tail = None