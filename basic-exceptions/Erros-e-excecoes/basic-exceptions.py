"""Some exemples of Syntax Errors!
This page contein pharses comented by quotation marks, and code by hash"""

# while True: print('Hello World')

"""After the error the current program is gonna be stoped,
i.e., in the first error!
Exceptions exemples:"""

# 10 * (1/0) error caused: ZeroDivisionError: division by zero
# 4 + spam*3 error caused: NameError: name 'spam' is not defined
# '2' + 2 error caused: TypeError: can only concatenate str (not "int") to str

"""Handling Exceptions!
See to a simgle exemple bellow"""

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Opa! That was no valid number. Try again...")

