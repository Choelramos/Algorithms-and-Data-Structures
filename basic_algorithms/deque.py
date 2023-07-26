# Learning about collections.deque

from collections import deque
deque(['a', 'b', 'c'])

deque('abc')
deque([{'data': 'a'}, {'data': 'b'}])

llist = deque("abcde")
print(llist)

llist.append('f')
print(llist)

llist.pop()
print(llist)

llist.appendleft('z')
print(llist)

llist.popleft()
print(llist)
print()

# Queues with linked lists

queue = deque()
print(queue)

queue.append("Joel")
queue.append("Matias")
queue.append("Julia")
print(queue)

# If you'd like take the first person in the queue, then you could something like this:

queue.popleft()
print(queue)

"""Stacks
In this example, i created an empty history object, ans every time the user visited a nes site,
i added it to your history variable using appendleft()"""

history = deque()
history.appendleft("https://google.com")
history.appendleft("https://youtube.com")
history.appendleft("https://stackoverflow.com")
print(history)
