"""I've study queues before, but never is bad weather to revise"""

from collections import deque
from heapq import heappop, heappush


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


class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, value))  # Python's heap is a min-heap. I use "-priority" to get around it

    def dequeue(self):
        return heappop(self._elements)[1]


"""
# Implemantation of FIFO
fifo = Queue("1st", "2nd", "3nd")
print(len(fifo))

for element in fifo:
    print(element)

print(len(fifo))
"""

"""
# Implementation of LIFO

lifo = Stack("1st", "2nd", "3nd")
for element in lifo:
    print(element)
"""


"""
# Implementation of Priority Queue.
In this case i defined a system of the an car priority as example"""

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messeges = PriorityQueue()
messeges.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messeges.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messeges.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messeges.enqueue_with_priority(IMPORTANT, "Hazerd lights turned on")

print(messeges.dequeue())








