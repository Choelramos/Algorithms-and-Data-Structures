# Ordenação pelo método bolha (bubblesort)
def trocar(seq, i):
    aux = seq[i]
    seq[i] = seq[i + 1]
    seq[i + 1] = aux


seq = [1, 5, 8, 15, 20, 4, 7, 2, 10, 18]

troca = 1
while troca:
    troca = 0
    i = 0
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            trocar(seq, i)
            troca = 1
print(seq)
