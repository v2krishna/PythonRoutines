"""
    == compares the values of the both operands
    is --- checks refers to the same object or not
    identity operator(is)
"""

x = y = 34678900010
print(id(x))
print(id(y))

print(x is y)


string_1 = "Hello"
string_2 = "Hello"

print(string_1 is string_2)