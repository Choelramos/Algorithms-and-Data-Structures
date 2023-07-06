
def buscaLista(k, L, n):
    i = 0
    indiceL = -1
    while i < n:
        if L[i] == k:
            indiceL = i
            i = n + 1
        i = i + 1
    return indiceL


l = ['Joel', 'Edisvanei', 'Cleberson']

buscando = buscaLista('Cleberson', l, len(l))
print(buscando)

# Outra forma
nomes = ['Joel', 'Edisvanei', 'Cleberson']
i = nomes.index('Edisvanei')
print(i)
