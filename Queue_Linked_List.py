from SingleLinkedList import singlelinkedlist
class Queue(singlelinkedlist):
    def __init__(self,size):
        super().__init__()
        self.max_size = size
        self.current_size = 0
    
    #Enqueue
    def enqueue(self,value):
        if self.current_size == self.max_size:
            print("Queue is full")
        else:
            self.addnode(value,pos=None)
            self.current_size+=1
    #Dequeue
    def dequeue(self):
        if self.current_size == 0:
            return False
        else:
            x = self.head.value
            self.remove_pos(0)
            self.current_size -=1
        return x
    #PrintQueue
    def print(self):
        self.printlist()

