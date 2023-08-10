# This exemple bellow show how to reference the different scopes and namespace
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment", spam)
    do_nonlocal()
    print("After local assignment", spam)
    do_global()
    print("After local assignment", spam)


scope_test()
print("In global scope", spam)


# Testing classes objects:
class MyClass:
    i = 12345

    def f(self):
        return "Hello World"


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(2.0, -4.5)


# Funcion defined outside the class
def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return "Hello World"
    h = g

# Methods call other methods


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

