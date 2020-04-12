"""
Using continue statement
"""
x = int(input("Enter a number"))
while x < 10:
    print(x)
    x += 1
    if x > 5:
        continue

print("End of the program")