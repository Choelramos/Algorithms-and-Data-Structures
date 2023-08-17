import timing_code as tm
from random import randint


# A basic implementarion of insertion sort
# I'm impresioned, it is so ingenious e-e
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


# Timing insertion sort implementation:

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(tm.ARRAY_LENGTH)]

    tm.run_sorting_algorithm(algorithm="insertion_sort", array=array)

