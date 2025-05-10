
# Chapter 7 Python Code - Task Scheduler (Priority Queue)
import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []

    def add_task(self, task, priority):
        heapq.heappush(self.heap, (priority, task))

    def get_task(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

ts = TaskScheduler()
ts.add_task('Task 1', 1)
ts.add_task('Task 2', 2)
print(ts.get_task())  # Output: 'Task 1'
