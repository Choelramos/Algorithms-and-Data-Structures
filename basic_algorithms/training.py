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


# Tests implements:

joel = Family('Joel', 27, 5000)
julia = Family('Julia', 22, 6000)

fam_string1 = 'Pandora-3-0'
fam_string2 = 'Matias-1-12000'

new_member = Family.from_string(fam_string1)

print(new_member.email)
print(julia.raise_amount)
print(joel.raise_amount)
# print(joel.__dict__)
