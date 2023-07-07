# Para inserir no final da lista
"""
def inserir(k, L, n):
    L.append('')
    L[n] = k
    n += 1

# Implementação


lista = [1, 2, 3, 4, 5]

inserir(6, lista, len(lista))

print(lista)
"""

# Para inserir em uma posição da lista


def inserreOrdenada(k, L, n):
    i = 0
    poInsercao = -1
    while i < n:
        if L[i] >= k:
            if L[i] == k:
                return -1
            else:
                poInsercao = i
                i = n + 1
        else:
            i = i + 1
        if i == n:
            poInsercao = n

    L.append('')
    i = n
    while i > poInsercao:
        L[i] = L[i - 1]
        i = i - 1
    L[poInsercao] = k
    return poInsercao


lista = [1, 3, 4, 5]
inserreOrdenada(2, lista, len(lista))
print(lista)

