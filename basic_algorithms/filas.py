""" Aqui colocarei alguns exemplos de inserção, busca e remoção em filas
Os métodos para insersão e remoção da lista contígua não foram implementados
É importante notar que o métodos busca (também não implementado), é identico da lista comum"""


class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class FilaEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio

    def print(self):
        current = self.inicio
        while current:
            print(current.valor)
            current = current.proximo

    def insere(self, novoNo):  # Inserindo na lista encadeada
        if self.inicio is None:
            self.inicio = novoNo
            self.final = novoNo
        else:
            self.final.proximo = novoNo
            self.final = novoNo

    def remove(self):  # Remoção do nó encadeado:
        if self.inicio is None:  # Underflow
            return None
        else:
            k = self.inicio
            self.inicio = self.inicio.proximo
            return k


# Enserindo na lista contígua:


"""
def insereFila(novoNo):
    global inicioFila
    global maxFila
    global finalFila
    global fila
    if inicioFila is None:
        fila[0] = novoNo
        inicioFila = 0
        finalFila = 0
    elif (finalFila + 1) % maxFila == inicioFila:  # Overflow
        return - 1
    else:
        finalFila = (finalFila + 1) % maxFila
        fila[finalFila] = novoNo
        return finalFila


# Remoção do nó lista contígua:

def removefila():
    global inicioFila
    global maxFila
    global finalFila
    global fila
    if inicioFila is None:
        return None
    k = fila[inicioFila]
    if finalFila == inicioFila:
        inicioFila = None
    else:
        inicioFila = (inicioFila + 1) % maxFila
    return k
"""
