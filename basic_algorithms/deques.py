# Aplicando deques
from collections import deque  # Dentro do Python temos a implementação

q = deque()
q.append('b')
q.append('c')
q.appendleft('a')
print(q)
print(q.popleft())
