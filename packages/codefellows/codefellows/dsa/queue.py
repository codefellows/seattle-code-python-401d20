from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def peek(self):
        return self.dq[-1]

    def is_empty(self):
        return len(self.dq) == 0

    def __len__(self):
        return len(self.dq)
