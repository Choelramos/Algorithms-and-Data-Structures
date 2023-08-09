"""In this file, I'll write the basic of OOP (Object-Oriented Programming)
Here you've finding many examples mixed, without order """

# The class dog to creat, a dog:


class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Pitbull(Dog):
    pass


class Pinshcer(Dog):
    pass


class Dogue(Dog):
    pass


pandora = Pitbull('Pandora', 2)  # instantiating the object
titica = Pinshcer('Titica', 10)
scooby = Dogue('Scooby Doo', 5)


print(pandora)
print(pandora.speak('Au au'))

print(type(pandora))  # show which class a given object belongs to
print(isinstance(pandora, Dog))  # The method says for yourself

