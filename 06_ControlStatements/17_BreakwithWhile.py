"""
Print n numbers and if n==5 stop the program to execute the remaining programs
"""
n = int(input("Enter the number:"))

while n != 1:
    print(n)
    if n == 5:
        break
    n -= 1
print("End of the program")