# Usando a alocação encadeada
"""
class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class PilhaEncadeada:
    def __init__(self, topo=None):
        self.topo = topo

    def push(self, novoNo):  # Inserção
        novoNo.proximo = self.topo
        self.topo = novoNo

    def pop(self):  # Remoção
        if self.topo is None:
            return None
        k = self.topo
        self.topo = self.topo.proximo
        return k
"""

# Alocação contígua Pilhas

maxPilha = 10
pilha = [None] * maxPilha
topoPilha = None


def push(novoNo):
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha is None:
        pilha[0] = novoNo
        topoPilha = 0
    elif topoPilha == maxPilha - 1:
        return -1
    else:
        topoPilha = topoPilha + 1
        pilha[topoPilha] = novoNo
    return topoPilha


def pop():
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha is None:
        return None
    else:
        k = pilha[topoPilha]
        if topoPilha == 0:
            topoPilha = None
        else:
            topoPilha = topoPilha - 1
        return k


print(pilha)
for i in range(10):
    push(i)
    print(pilha)

print(push(11))
for i in range(10):
    print(pop())
print(pop())
