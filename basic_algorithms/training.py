import datetime


class Family:
    raise_amount = 1.05
    num_of_members = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.email = name + '.' + str(age) + '@' + 'family.com'
        self.salary = salary
        Family.num_of_members += 1

    def full_information(self):
        return f'Name: {self.name}, Age: {self.age}, email: {self.email}, salary: {self.salary}'

    def apply_raise(self):
        self.salary = int(self.salary + self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Make a new member of family from classmethod
    @classmethod
    def from_string(cls, fam_string):
        name, age, salary = fam_string.split('-')
        return cls(name, age, salary)

    # To know if the people in the family are busy
    @staticmethod
    def is_busy(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False


# Test Inheritance
class Son(Family):
    def __init__(self, name, age, salary, school):
        super().__init__(name, age, salary)
        self.school = school

    @staticmethod
    def is_at_school(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return False


class Pets(Family):
    def __init__(self, name, age, animal='dog', pets=None):
        super().__init__(name, age, animal)
        self.animal = animal
        if pets is None:
            self.pets = []
        else:
            self.pets = pets

    def add_dog(self, pet):
        if pet not in self.pets:
            self.pets.append(pet)

    def rem_dog(self, pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def sit_down(self):
        return print(self.name + ' is sit down!')

    def roll(self):
        return print(self.name + ' is rolling')


# Tests implements:
joel = Family('Joel', 27, 50000)
julia = Family('Julia', 22, 60000)

pandora = Pets('Pandora', 3)

print(pandora.animal)
