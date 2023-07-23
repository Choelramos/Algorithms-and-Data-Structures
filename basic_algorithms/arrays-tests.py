"""I'm learning about arrays, I've like that!
To find a specific knowledge, I've separate for # the topics"""
import array
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
print()

# To remove items, I'll use remove and pop methods:

arry = arr.array('i', [1, 2, 3, 4, 5])
print("The new created array is : ", end=" ")
for i in range(0, 5):
    print(arry[i], end=" ")

print("\r")

print("The popped element is: ", end=" ")
print(arry.pop(4))

print("The array after popping is:", end=" ")
for i in range(0, 4):
    print(arry[i], end=" ")

print("\r")

arry.remove(1)  # In this case I remove the number 1 of the array, not index 1
print("After to remove method: ", end=" ")
for i in range(0, 3):
    print(arry[i], end=" ")
print()
print()


# Slincing elements

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ar = arr.array('i', l)
print("Initial array: ")
for i in ar:
    print(i, end=" ")

sliced_array = ar[3:8]
print("\nElements sliced in a range 3-8: ", end=" ")
print(sliced_array)

sliced_array = ar[5:]
print("Elements sliced from 5th element till the end: ", end=" ")
print(sliced_array)

sliced_array = ar[:]
print("Printing all elements using slice operation: ", end=" ")
print(sliced_array)
print()
print()

# Searching the elements in array:
# I'll use the same array above
print("The array created is: ", end=" ")
for i in range(0, 10):
    print(ar[i], end=" ")
print("\r")

print("The index of 1st occurence of 2 is: ", end=" ")
print(ar.index(2))
print("The index of 1st occurence of 1 is: ", end=" ")
print(ar.index(1))

# Counting elements in an Array:
my_array = array.array('i', [1, 2, 3, 4, 5, 2, 3, 2])
count = my_array.count(2)
print("Number of occurrences of 2: ", count)

# Reverse Elements:
print("Original Array: ", *my_array)
my_array.reverse()
print("Reversed array:", *my_array)

