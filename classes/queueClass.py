from collections import deque

"""
    Implémentation manuel d'une structure de file à partir du module Deque
"""


class Queue:

    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
