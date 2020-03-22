str1 = "Strings functions used in this program"
str2 = "string to compare"
print(str1)
print("length of the string {}".format(len(str1)))
print("Compare the strings ")

print(str1 is str2)
print(str2 == str1)
print(str2 in str1)

print("reverse the string")
print(str1[::-1])

print("Concatenate str1 and str2: ", str1 + " " + str2)
print("Ucase of the string 1 ", str1.upper())
print("Lcase of the string 2 ", str2.lower())

str1, str2 = str2, str1
print(str1)
print(str2)
print(str1.swapcase())
