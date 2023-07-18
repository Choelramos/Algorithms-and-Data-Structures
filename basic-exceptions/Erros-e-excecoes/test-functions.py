"""This way the function woll receive a tuple of arguments, and can access the items accordingly"""


def myfunction(*name):
    print("The name is " + name[1])


myfunction("Jo", "Ju", "Ma")


"""Arbitrary Keyword Arguments, **kwargs
The way the function will receive a dictionary of arguments,
and can access the items accordingly:"""


def my_other_functio(**name):
    print("Hes first name is: " + name["first"])


my_other_functio(name="Ju Ju", first="Ju")


"""Default parameter Value
If we call the function without argument, it uses the default value"""


def another_function(country="Brasil"):
    print("I am from " + country)


another_function()
another_function("Japan")


"""A sample list of arguments"""


def function_list(food):
    for x in food:
        print(x)


fruits = ["Banana", "Aple", "Orange"]
function_list(fruits)


