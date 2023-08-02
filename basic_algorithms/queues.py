"""I've study queues before, but never is bad weather to revise"""

from collections import deque


class Queue:
    def __init__(self, *elements):  # Optionally accept initil elements (*)
        self._elements = deque(elements)  # The leading undercore in the attribute's name indicates an internal bit of
        # implementation which only the class should access and modify

    def __len__(self):  # return the length of the elements
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3nd")

print(fifo.dequeue())
