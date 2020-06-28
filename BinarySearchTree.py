class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    # Insert funtion Recursive
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
    # Search Function
    def search(self,data):
        if self.data == data:
            return True
        elif self.data>data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
    # Delete Function
    def delete(self,data):
        parent = None
        node = self
        # Search for the element to delete
        while node.data != data:
            if data <node.data and node.left:
                parent = node
                node = node.left
            elif data>node.data and node.right:
                parent = node
                node = node.right
            else:
        # Case 1: If data is not found
                return False

        # Node to be deleted is now found
        # Case 2: node which has to be deleted has no children
        if node.left == None and node.right == None:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            return True
        # Case 3: node has no left child but has right child
        elif node.left == None and node.right:
            if parent.left is node:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        # Case 4: node has no right child but has left child
        elif node.right == None and node.left:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        # Case 5: node has both left and right child
        else:
            delnodeparent = node
            delnode = node.right
            while delnode.left:
                delnodeparent = delnode
                delnode = delnode.left
            node.data = delnode.data
            # Now case arises that if delnode has only right child or no child
            # Since delnode is succesor of node and successor does not have any left child
            if delnode.right:
                if delnodeparent.right is delnode:
                    delnodeparent.right = delnode.right
                else:
                    delnodeparent.left = delnode.right
            else:
                if delnodeparent.right is delnode:
                    delnodeparent.right = None
                else:
                    delnodeparent.left = None

            return True
    # Preorder Traversal
    def preorder(self):
        if self:
            print(self.data)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    # Inorder Traversal
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.data)
            if self.right:
                self.right.inorder()
    # Postorder Traversal           
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
    # Insert Function
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
    # Extend Function
    def extend(self,lst):
        for i in lst:
            self.insert(i)
    # Search Function
    def search(self,data):
        if self.root:
            return self.root.search(data)
        else:
            return False
    # Delete Function
    def delete(self,data):
        if self.root is None:
            return False
        # If root.data == data
        elif self.root.data == data:
            # Case 1: root is the only element in bst
            if self.root.left == None and self.root.right == None:
                self.root = None
            # Case 2: if root node has only left child then set root as root.leftchild
            elif self.root.left and self.root.right == None:
                self.root = self.root.left
            # Case 3: if root node has only right child then set root as root.rightchild
            elif self.root.right and self.root.left == None:
                self.root = self.root.right
            # Case 4:  if root has both children
            elif self.root.right and self.root.left:
                # Find successor of root
                delnodeparent = self.root
                delnode = self.root.right
                while delnode.left:
                    delnodeparent = delnode
                    delnode = delnode.left
                self.root.data = delnode.data
                if delnode.right:
                    if delnodeparent.right is delnode:
                        delnodeparent.right = delnode.right
                    else:
                        delnodeparent.left = delnode.right
                else:
                    if delnodeparent.right is delnode:
                        delnodeparent.right = None
                    else:
                        delnodeparent.left = None

        else:
            return(self.root.delete(data))
    # Preorder Traversal
    def preorder(self):
        if self.root == None:
            print("Tree is empty")
        else:
            print("Preorder Traversal")
            self.root.preorder()
    # Inorder Traversal
    def inorder(self):
        if self.root == None:
            print("Tree is empty")  
        else:      
            print("Inorder Traversal")
            self.root.inorder()
    # Postorder Traversal
    def postorder(self):
        if self.root == None:
            print("Tree is empty")
        else:
            print("Postorder Traversal")
            self.root.postorder()

