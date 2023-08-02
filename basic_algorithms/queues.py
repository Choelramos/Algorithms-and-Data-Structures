"""I've study queues before, but never is bad weather to revise"""

from collections import deque


class Queue:
    def __init__(self, *elements):  # Optionally accept initil elements (*)
        self._elements = deque(elements)  # The leading undercore in the attribute's name indicates an internal bit of
        # implementation which only the class should access and modify

    def __len__(self):  # return the length of the elements
        return len(self._elements)

    def __iter__(self):  # If this, you'll make your class intances usable in a for loop
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


"""
# Implemantarion of FIFO
fifo = Queue("1st", "2nd", "3nd")
print(len(fifo))

for element in fifo:
    print(element)

print(len(fifo))
"""

"""
# Implementation of LIFO
"""

lifo = Stack("1st", "2nd", "3nd")
for element in lifo:
    print(element)

