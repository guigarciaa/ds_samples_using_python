class Stack:
    def __init__(self):
        self.items = [] # create an empty list
        self.items = self.items[:9] # limit the stack to 10 items

    def push(self, item):
        if len(self.items) < 10:
            self.items.append(item)
        else:
            raise IndexError("Stack is full")
