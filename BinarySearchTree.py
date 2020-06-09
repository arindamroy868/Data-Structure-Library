class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def insert(self,data):
        if self.data == data:
            return False
        elif self.data>data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    
    def find(self,data):
        if self.data == data:
            return True
        elif self.data>data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    def preorder(self):
        if self:
            print(self.data)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
        
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.data)
            if self.right:
                self.right.inorder()
                
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data)


class binarysearchtree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder(self):
        print("Preorder Traversal")
        self.root.preorder()

    def inorder(self):
        print("Inorder Traversal")
        self.root.inorder()

    def postorder(self):
        print("Postorder Traversal")
        self.root.postorder()

#if __name__ == "__main__":
