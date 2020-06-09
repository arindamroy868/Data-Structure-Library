class Node:
    def __init__(self,init_data=None):
        self.data = init_data
        self.next = None
        self.prev = None
    def get_data(self):
        return self.data
    def set_data(self,new_data):
        self.data = new_data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def set_next(self,new_next):
        self.next = new_next
    def set_prev(self,new_prev):
        self.prev = new_prev

