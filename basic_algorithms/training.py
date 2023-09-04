class Family:

    gain_point = 1
    num_of_members = 0

    def __init__(self, name, age, points):
        self.name = name
        self.age = age
        self.email = name + '.' + str(age) + '@' + 'family.com'
        self.points = points
        Family.num_of_members += 1

    def full_information(self):
        return f'Name: {self.name}, Age: {self.age}, email: {self.email}, points: {self.points}'

    def gain_points(self):
        self.points = int(self.points + self.gain_point)


# Tests implements:
joel = Family('Joel', 27, 1)
julia = Family('Julia', 22, 1)
joel.gain_points()

print(Family.num_of_members)

print(julia.full_information())
print(joel.full_information())
# print(joel.__dict__)
