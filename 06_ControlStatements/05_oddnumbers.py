"""
Display odd numbers between two numbers using for loop
"""
m, n = [int(x) for x in input("Enter two numbers").split()]
if m < n:
    pass
else:
    m, n = n, m
print("Entered numbers are {0} and {1}".format(m, n))
for i in range(m, n):
    if i % 2 !=0:
        print(i)

print("End of the program")