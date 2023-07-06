# Adicionando a lista ordenada
# Inserindo na lista e empurrado os elementos para frente

def insereOrdenada(k, L, n):
    i = 0
    posInsercao = - 1
    while i < n:
        if L[i] >= k:
            if L[i] == k:
                return -1
            else:
                posInsercao = i
                i = n + 1
        else:
            i = i + 1
        if i == n:
            posInsercao = n

    L.append('')
    i = n
    while i > posInsercao:
        L[i] = L[i - 1]
    i = i - 1
    L[posInsercao] = k
    return posInsercao


lista = [1, 3, 2, 5, 7, 6]
sla = insereOrdenada(5, lista, 1)
print(sla)
print(lista)
