from Node import Node
class unorderedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add(self,item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.set_next(Node(item))
            self.tail = self.tail.get_next()

    def size(self):
        count = 0
        current = self.head
        while current.get_next() != None:
            count += 1
            current = current.get_next()
        return count+1

    def search(self,item):
        current = self.head
        while current.get_data() != item and current.get_next() != None:
            current = current.get_next()
        return current.get_data() == item

    def remove(self,item):
        if self.head == None:
            print("List is empty")
            return None
        current = self.head
        prev = None
        found = False

        #Loop till element is found in list or the list ends
        while not found and current != None:
            # If element found in list break loop
            if current.get_data() == item:
                found = True
            else:
                prev = current
                current = current.get_next()
        #If list has only one element initially then prev will remain None
        if prev == None:
            # Since prev is None then head is the only element in list
            # If head has value equal to item then set head as None
            if self.head.get_data() == item:                
                self.head = current.get_next()
            #Else print that element not found in the list
            else:
                print("Element Not in List")
        # If the element was found then and only then the prev will be set to Next element of Current in the list        
        elif found:
            prev.set_next(current.get_next())
        

    def print_list(self):
        if self.is_empty():
            print("list is Empty")
            return None
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()

if __name__ == "__main__":
    ul = unorderedlist()
    ul.add(1)
    ul.add(2)
    ul.add(3)
    ul.print_list()
    ul.remove(3)
    ul.print_list()
