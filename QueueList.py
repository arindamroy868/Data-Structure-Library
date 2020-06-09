class queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)