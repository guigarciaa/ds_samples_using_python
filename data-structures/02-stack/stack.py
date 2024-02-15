# Items are pushed into the top of a stack
# Items are popped from the top of a stack
# The stack is limited to 5 items
# A last in first out data structure (LIFO)
# A stack is an  abstract data type (ADT)

class Stack:
    def __init__(self):
        self.items = [] # create an empty list
        self.items = self.items[:5] # limit the stack to 5 items
    
    def push(self, item):
        if self.__isFull():
            raise IndexError("Stack is full")
        self.items.append(item)
        return self.items;
            
    def pop(self):
        if self.__isEmpty():
            raise IndexError("Stack is empty")
        self.items.pop()
        return self.items
    
    def peek(self):
        return self.items[len(self.items) - 1]

    def __isFull(self):
        return len(self.items) == 5
    
    def __isEmpty(self):
        return self.items == []
    

stack = Stack()
print(stack.push("Alice"))
print(stack.push("Bob"))
print(stack.push("Charlie"))
print(stack.push("David"))
print(stack.push("Eve"))
#print(stack.push("Frank")) # IndexError: Stack is full

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
#print(stack.pop()) # IndexError: Stack is empty

