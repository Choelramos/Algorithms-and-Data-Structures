class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.email = name + '.' + str(age) + '@' + 'family.com'

    def full_information(self):
        return f'Name: {self.name}, Age: {self.age}, email: {self.email}'


joel = Family('Joel', 27)
julia = Family('Julia', 22)

print(joel.full_information())

