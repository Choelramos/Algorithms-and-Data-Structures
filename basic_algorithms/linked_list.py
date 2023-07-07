# Classe com implementação de linked list, com operações de busca, inserção e remoção

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def print(self):
        current = self.cabeca
        while current:
            print(current.valor)
            current = current.proximo

    def busca(self, k):
        noAtual = self.cabeca
        if noAtual.chave == k:
            return noAtual
        while noAtual.proximo is not None:
            noAtual = noAtual.proximo
            if noAtual.chave == k:
                return noAtual
            return None

    def insereInicio(self, novoNo):
        novoNo.proximo = self.cabeca
        self.cabeca = novoNo

    def insereFinal(self, novoNo):
        noAtual = self.cabeca
        if noAtual:
            while noAtual.proximo:
                noAtual = noAtual.proximo
            noAtual.proximo = novoNo
        else:
            self.cabeca = novoNo

    def removeLista(self, k):
        noAtual = self.cabeca
        if noAtual is None:
            return None
        if noAtual.chave == k:
            self.cabeca = noAtual.proximo
            return 0
        noAnterior = noAtual
        noAtual = noAtual.proximo
        while noAtual is not None:
            if noAtual.chave == k:
                noAnterior.proximo = noAtual.proximo
                return k
            else:
                noAnterior = noAtual
                noAtual = noAtual.proximo
        return - 1

    def insereOrdenada(self, novoNo):
        noAtual = self.cabeca
        if noAtual.chave > novoNo.chave:
            novoNo.proximo = self.cabeca
            self.cabeca = novoNo
            return 0
        if noAtual.proximo is not None:
            while noAtual.chave < novoNo.chave:
                if noAtual.proximo is None:
                    noAtual.proximo = novoNo
                    return 0
                noAnterior = noAtual
                noAtual = noAtual.proximo
        novoNo.proximo = noAtual
        noAnterior.proximo = novoNo


# Testando implementação


e0 = No(0, 'Zeus')
Lista = ListaEncadeada(e0)
k0 = Lista.busca(0)
print(k0.valor)

print()

e1 = No(1, 'Poseidon')
Lista.insereFinal(e1)
Lista.print()

print()

e2 = No(-1, 'Hades')
Lista.insereInicio(e2)
Lista.print()

print()

e3 = No(1, 'Ares')
Lista.insereOrdenada(e3)
Lista.print()
