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

#while True:
#   try:
#        x = int(input("Please enter a number: "))
#        break
#    except ValueError:
#        print("Opa! That was no valid number. Try again...")


"""The most common pattern for handling Exception is to print or log the exception
and then re-raise it (allowing a caller to handle the excepition as well)"""

import sys
#try:
#    f = open('myfile.txt')
#    s = f.readline()
#    i = int(s.strip())
#except OSError as err:
#    print("OS error:", err)
#except ValueError:
#    print("Could not convert data to an integer.")
#except Exception as err:
#    print(f"unexpected {err}, {type(err)=}")

"""The else clause. It is useful for code that must be executed if the try clause
does note raise on exception. For exemple:"""
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print("Cannot open", arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()


