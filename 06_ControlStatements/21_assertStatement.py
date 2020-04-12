"""
Assert statement is used to check a condition and throws AssertionError
"""
x = int(input("Enter a number:"))
print(x)
assert (x>0), "Wrong Number Entered"
print("Entered number is ", x)