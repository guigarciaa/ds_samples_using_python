class Node:
    def __init__(self, data):
        self.data = data
        self.nest = None
        

class LinkedList:
    def __init__(self):
        self.linked_list = [];

    def offer(self, value):
        if self.isFull():
            raise Exception("List is full")
        self.linked_list.insert(value)
