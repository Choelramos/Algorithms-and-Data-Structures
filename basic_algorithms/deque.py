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

