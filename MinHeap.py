# Importing Sys library for getting max possible numerical value
import sys
# MinHeap Class
class MinHeap:
    # Initializing Minheap attributes
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        # Creating empty heap and setting each element equal to 0
        self.heap = [0]*(self.maxsize+1)
        # Setting 0th element as -max possible value
        self.heap[0] = -1*sys.maxsize
        self.FRONT = 1
    # Returns the position of parent 
    def getParent(self,pos):
        return (pos//2)
    # Returns the position of leftchild
    def getLeftchild(self,pos):
        return (2*pos)
    # Returns the poition of rightchild
    def getRightchild(self,pos):
        return (2*pos + 1)
    # Check if node is leaf node or not, if position is greater than half of size of heap and less than or equal to size of heap then it is leaf node
    # Else it is non-leaf node
    def isleaf(self,pos):
        if pos>self.size//2 and pos<=self.size:
            return True
        return False
    # Insert the value in min heap at last postion then rearranges the nodes in bottom to top order in order to maintain min heap property
    def insert(self,data):
        self.size = self.size + 1
        self.heap[self.size] = data
        current = self.size
        while self.heap[self.getParent(current)]>self.heap[current]:
            self.heap[current],self.heap[self.getParent(current)] = self.heap[self.getParent(current)],self.heap[current]
            current = self.getParent(current)
    # Function to quickly insert list of numbers in minheap
    def extend(self,lst):
        for i in lst:
            self.insert(i)
    # Prints the minheap with parents and childrn info
    def printheap(self):
        for i in range(1,self.size):
            if not self.isleaf(i):
                print("Parent : " + str(self.heap[i]) + "\n" +
                    "Left Child : " + str(self.heap[2*i])+ "\n" + 
                    "Right Child : " + str(self.heap[2*i + 1])+ "\n")
            else:
                break
    # Peek the top element of minheap
    def getmin(self):
        if self.size == 0:
            return False
        return self.heap[self.FRONT]
    # Swap the data of two nodes
    def swap(self,fpos,spos):
        self.heap[fpos],self.heap[spos] = self.heap[spos],self.heap[fpos]
    # Minheapify means rearranging in top to bottom order
    def Minheapify(self,pos):
        current = pos
        left = self.getLeftchild(current)
        right = self.getRightchild(current)
        if not self.isleaf(current):
            if self.heap[current]>self.heap[left] or self.heap[current]>self.heap[right]:
                if self.heap[left]<self.heap[right]:
                    self.swap(current,left)
                    self.Minheapify(left)
                elif self.heap[right]<self.heap[left]:
                    self.swap(current,right)
                    self.Minheapify(right)   
    # Returns the min value in minheap that is top value
    def extractmin(self):
        if self.size == 0:
            return False
        else:
            popped = self.heap[self.FRONT]
            self.heap[self.FRONT] = self.heap[self.size]
            self.size -= 1
            self.Minheapify(self.FRONT)
            return popped


