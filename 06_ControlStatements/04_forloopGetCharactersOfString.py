"""
    Retrieve the characters of string using for loop
"""
str = input("Enter the string")
for ch in str:
    print(ch)

print("using the length of the string")
n = len(str)
for i in range(n):
    print(str[i])
