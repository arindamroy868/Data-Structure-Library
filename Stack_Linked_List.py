from SingleLinkedList import singlelinkedlist
class Stack(singlelinkedlist):
    def __init__(self,size):
        super().__init__()
        self.max_depth = size
        self.depth = 0

    def push(self,value):
        if self.depth == self.max_depth:
            print("Stack is Full, can't push more elements")
        else:
            self.addnode(value,0)
            self.depth += 1

    def peek(self):
        print(self.head.value)
    
    def pop(self):
        if self.depth == 0:
            print("Stack Empty")
        else:
            print(self.head.value)
            self.remove_pos(0)

    def isempty(self):
        if self.head is self.tail:
            print("True")
        else:
            print("False")
    
    def isfull(self):
        if self.depth == self.max_depth:
            print("True")
        else:
            print("False")

    def deletestack(self):
        self.deletelist()

    def print(self):
        self.printlist()
