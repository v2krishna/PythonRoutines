"""
Find wheter a given number is even or odd
"""

x = float(input("Enter a integer/float number:"))

if x % 2 == 0:
    print("Given input {0} is even number".format(x))
else:
    print("Given input {0} is odd number:".format(x))

print("End of if statements")