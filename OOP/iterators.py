# Some example about operations of iterators

class MyNumbers:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):  # method to iter into this class
        self.a = 1
        return self

    def __next__(self):  # It speaks for itself
        x = self.a
        if x > self.limit:
            raise StopIteration
        self.a += 1
        return x


myclass = MyNumbers(10)
myiter = iter(myclass)
print(next(myiter))
print()

for i in myclass:
    print(i)

