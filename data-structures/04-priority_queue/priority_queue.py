import random
import string

class PriotityQueue:
    def __init__(self, reverse=False):
        self.queue = []
        self.queue = self.queue[:5]
        self.isReverse = reverse

    def offer(self, value):
        if self.isFull():
            raise IndexError("Queue is Full")
        self.queue.append(value);
        self.queue.sort(reverse=self.isReverse)
        return self.queue

    def poll(self):
        if self.isEmpty():
            raise IndexError("Queueis Empty")
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def isFull(self):
        return len(self.queue) == 5
    
    def isEmpty(self):
        return self.queue == []


new_priorityQueue = PriotityQueue()

# for x in range(6):
#     if not new_priorityQueue.isFull():
#         random_float = round(random.uniform(1.0, 10.5), 2)
#         print(new_priorityQueue.offer(random_float))

for x in range(6):
    if not new_priorityQueue.isFull():
        print(new_priorityQueue.offer(random.choice(string.ascii_lowercase)))

while not new_priorityQueue.isEmpty():
      print(new_priorityQueue.poll())