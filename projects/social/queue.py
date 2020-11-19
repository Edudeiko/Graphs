# Note: This Queue class is sub-optimal. Why?
from collections import deque


class Queue():
    def __init__(self):
        self.queue = deque()  # collection deque

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.popleft()
        else:
            return None

    def size(self):
        return len(self.queue)
