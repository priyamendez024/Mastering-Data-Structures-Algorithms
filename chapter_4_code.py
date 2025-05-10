
# Chapter 4 Python Code - Queue Implementation
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
