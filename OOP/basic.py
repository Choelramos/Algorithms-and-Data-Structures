"""In this file, I'll write the basic of OOP (Object-Oriented Programming)
Here you've finding many examples mixed, without order """

# The class dog to creat, a dog:


class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


pandora = Dog('Pandora', '2', 'Pitbull')
print(pandora)

print(pandora.breed)
print(pandora.speak('Au au'))
