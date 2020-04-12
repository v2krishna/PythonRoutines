"""
Assert Statement with try .. except
"""
x = int(input("Enter a numbers"))
try:
    assert(x>0)
    print("Entered numbered is :", x)
except AssertionError:
    print("Entered the wrong number")