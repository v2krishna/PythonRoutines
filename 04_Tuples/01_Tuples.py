"""
    Tuples are one more data types
    Once created , cannot be able to add, delete, replace  , reorder elements.
    Sequence types
    Holds any data type.
    Tuples are immutables
    Faster than lists.
    Duplicate elements are allowed
"""

tuple_1 = (1, 2, 3, 4, 5, 6)
print(tuple_1)

print(len(tuple_1))

print(id(tuple_1))

t2 = (1, 2, 3, 4, 5, 'String Example', "python")
print(t2)

t3 = ([1, 2, 3 , 75], [34, 35, 36])
print(t3)

print(t3[1])
print(t3[1][1])

print(min(t3), max(t3))