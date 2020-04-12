"""
Find even numbers between two numbers
"""

m, n = [int(x) for x in input("Enter two numbers").split(" ")]
print(m, n)
if m > n:
    m, n = n, m
else:
    m, n = m, n

while m <= n:
    if m % 2 == 0:
        print(m)
    m += 1
print("End of the program")