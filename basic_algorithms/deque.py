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
print('\n')

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
print('\n')


"""Stacks
In this example, i created an empty history object, ans every time the user visited a nes site,
i added it to your history variable using appendleft()"""

history = deque()
history.appendleft("https://google.com")
history.appendleft("https://youtube.com")
history.appendleft("https://stackoverflow.com")
print(history)
print('\n')
# My own linked list

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
            
# An exemple using the aboe classes:


llist = LinkedList()
print(llist)
first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)
"""

# In exemple below I can create linked lists faster


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


llist = LinkedList(["0", "1", "2", "3", "4", "5"])
print(llist)
