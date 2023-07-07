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














