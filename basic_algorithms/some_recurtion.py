from timeit import timeit


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


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


a = [5, 2, 9, 4, 1, 3]

print(merge_sort(a))
