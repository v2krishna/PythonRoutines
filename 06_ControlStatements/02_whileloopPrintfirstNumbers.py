"""
Take the user input and print first n numbers
"""
n = int(input("Enter an integer number:"))
print(n)
x = 1
while x <= n:
    print(x, sep=" ")
    x += 1
print("End of the program")