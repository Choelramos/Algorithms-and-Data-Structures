def busca(procura, lista, tamanho_lista):
    i = 0
    indice_lista = -1
    while i < tamanho_lista:
        if lista[i] >= procura:
            if lista[i] == procura:
                indice_lista = i
                i = tamanho_lista + 1
            else:
                i = tamanho_lista + 1
        else:
            i = i + 1
    return indice_lista


l = [1, 2, 3, 5, 7]
usando = busca(9, l, len(l))

print(usando)

