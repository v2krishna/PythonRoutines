"""
Strings
  -- Immutable, cant be changed through out the program
  -- Class of type str
  -- its not a primitive data type
  -- Dis

Operations performed on the String
    > concat
    > slicing str[start:end:step] -- subset of string from the whole string
    > indexing
    > comparision operators
"""

str1 = "Welcome to Python"

print("memory location {}".format(id(str1)))
print("Type of the string {}".format(type(str1)))
print("Length of the string {}".format(len(str1)))
print(str1[1])
print(str1[0::2])
print(str1[1:3])
print(str1[:14])
print(str1[4:])

ch = 'A'
print(ord(ch))
print("to know the ascii values of {}".format(chr(65)))

"""
    comparision operators
"""
print("Welcome" in str1)
print("welcome" in str1)
print("welcome" != str1)
print("welcome" > str1)


str2 = str("test the string is created or not")
print(str2)
