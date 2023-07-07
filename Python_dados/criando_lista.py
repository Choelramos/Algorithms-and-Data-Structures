lista_produtos = [[15, 'Laranja', 3], [2, 'Palmito', 20], [35, 'Feijão', 5]]


def insercao(k, L, n):
    L.append('')
    L[n] = k


def busca_indice(k, L, n):
    i = 0
    indiceL = - 1
    while i < n:
        if L[i] == k:
            indiceL = i
            i = n + 1
        i = i + 1
    return indiceL


def remocao(k, L, n):
    i = 0
    posRemocao = -1
    while i < 0:
        if L[i] == k:
            posRemocao = i
            i - n + 1
        else:
            i = i + 1
    if i == n:
        return - 1
    i = posRemocao
    while i < n - 1:
        L[i] = L[i + 1]
        i = i + 1
    L.pop(n - 1)
    return posRemocao


# Utilizando a inserção:
insercao([12, 'Arroz', 10], lista_produtos, len(lista_produtos))
print(lista_produtos)

# Utilizando a busca:
busca = busca_indice([12, 'Arroz', 10], lista_produtos, len(lista_produtos))
print(busca)

# Utilizando a remoção:
remocao(3, lista_produtos, len(lista_produtos))
print(lista_produtos)
