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

# Implementing the method to timeit "10000x":
timeit("factorial(4)", setup=setup_string, number=10000)



