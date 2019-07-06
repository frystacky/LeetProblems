

class Node(object):

    def __init__(self,data = None,next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size (self):
        return self.size
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size +=1
    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.remove(8)
print(myList.remove(12))
print(myList.find(5))

        
        
        
        
