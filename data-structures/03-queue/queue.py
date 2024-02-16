class Queue:
    def __init__(self):
        self.queue = []
        self.queue = self.queue[:5]

    def enqueue(self, item):
        if self.__isFull():
            raise IndexError("Queue is full")
        self.queue.append(item)
        return self.queue
    
    def dequeue(self):
        if self.__isEmpty():
            raise IndexError("Queue is empty")
        self.queue.pop(0)
        return self.queue
    
    def peek(self):
        return self.queue[0]
    
    def __isFull(self):
        return len(self.queue) == 5
    
    def __isEmpty(self):
        return self.queue == []
    
queue = Queue()
print(queue.enqueue("Alice"))
print(queue.peek())
print(queue.enqueue("Bob"))
print(queue.enqueue("Charlie"))
print(queue.enqueue("David"))


print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
# print(queue.dequeue()) # IndexError: Queue is empty