"""I'm learning about arrays, I've like that!"""
import array as arr

a = arr.array('i', [10, 20, 30])

print("Array a before insertion:", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# How to insert values, using two methods built-in:
a.insert(3, 40)  # inserto is used to insert one or more data elements into an array
a.append(50)

print("Array after insertion: ", end=" ")
for i in a:
    print(i, end=" ")
print()
print()
#  =========================================================================================================

b = arr.array('d', [1.0, 2.0, 3.0])
b.append(4.0)

print("Array b before insertion", end=" ")
for i in range(1, 3):
    print(b[i], end=" ")
print()


print("Array b after insertion: ", end=" ")
for i in b:
    print(i, end=" ")
print()
