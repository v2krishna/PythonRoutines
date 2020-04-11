"""
Enter two numbers and find sum
Use only one input function to enter the numbers
list comprehension
"""

a, b, c = [int(x) for x in input("Enter three numbers:").split()]
print("sum of three numbers: ", a+b+c)