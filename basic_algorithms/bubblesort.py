import timing_code as tm
from random import randint

# Ordenação pelo método bolha (bubblesort)
"""
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
"""


# Another method of Bubble sort algorithm
def bubble_sort(array):
    n = len(array)

    for x in range(n):
        already_sorted = True

        for y in range(n - x - 1):
            if array[y] > array[y + 1]:
                array[y], array[y + 1] = array[y + 1], array[y]
                already_sorted = False

        if already_sorted:
            break

    return array


# Testing using timing_code imported
if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(tm.ARRAY_LENGTH)]

    tm.run_sorting_algorithm(algorithm="bubble_sort", array=array)


# My implementation:
print()
arr = [5, 3, 8, 9, 1, 2]
i = bubble_sort(arr)
print(i)
