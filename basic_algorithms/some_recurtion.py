from random import randint
from timing_code import run_sorting_algorithm


# Simple function to count down to zero
def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)
        return


# A more concise countdown
def countdown2(n):
    print(n)
    if n >= 0:
        countdown(n - 1)


# A non-recursive implementation for comparison:
def countdown3(n):
    while n > 0:
        print(n)
        n -= 1


# A simple recursion function
def factorial0(n):
    return 1 if n <= 1 else n * factorial0(n - 1)


# Another exemple of factorial using for loop:
def factorial2(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value


# There another method using the reduce(), but I don't explain here

# Using timeit to compatasion implementations
"""First I'll timeit recursive factorial"""

setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""

""" Implementing the method to timeit "10000x":
print(timeit("factorial(4)", setup=setup_string, number=10000))
"""

# Iterative implementation
setup_string2 = """
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value

# Implementation:
print(timeit("factorial(4)", setup=setup_string2, number=10000))
"""
"""=================================================================================================================="""


# I'll create below, two different functions for Merge Sort
# Function to merge two different arrays:
def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


# Here I'll divide up over two the array
def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


""" Implementation and timeit Merge Sort
a = [5, 2, 9, 4, 1, 3]

print(merge_sort(a))


ARRAY_LENGTH = 1000
# Let's go timing this Merge Sort
if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="merge_sort", array=array)
=================================================================="""


# Now, I will implement the Quick Sort Algorithm
def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


"""My implementation of quicksort
a = [5, 6, 1, 2, 8, 3, 4, 7]
print(quicksort(a))

"""

# Now, I'll traverse a list of names and pick up the leafs

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

"""Some tests to understand if it is an instance
print(names)
print(isinstance(names[1][1], list))
print(names[1][1])
print()
"""


# Function to count leaf elements
def count_leaf_items(item_list):
    count = 0
    print(f"List: {item_list}")
    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += count_leaf_items(item)
        else:
            print(f"Conted leaf item \"{item}\"")
            count += 1

    print(f"-> Returning count {count}")
    return count


# Implementation
print(count_leaf_items(names))

