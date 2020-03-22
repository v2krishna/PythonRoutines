"""
Creating List
accessing elements in list
common operators
slicing
+ and * operators in lsit
in and not in operator
traversing list using loop
list method
list comprehension
"""

"""
Creating the lists
"""
l1 = list()
l1 = [1, 3, 4, 5, 6]
l2 = ["this", "is", "string", 12]
l3 =list("python")
print(l3)

print(l3[1])
print(l3[::-1])
print(len(l3))

print(max(l3))
print(min(l3))

l4 = [1, 2334, 5445645, 5445646]
print(max(l4))
print(min(l4))

# concatenate two lists
l5 = l3 + l4
print(l5)

# repeats the list elements by after the * operator
print(l2 * 3)

# slicing the list elements
print(l5[0:4])

# in and not in operator
print(l3)
print(l5)
print(l3 not in l5)