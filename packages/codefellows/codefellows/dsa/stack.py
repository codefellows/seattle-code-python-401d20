from collections import deque

class Stack:

    def __init__(self, values=""):
        self.storage = deque(values)

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return str(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0


