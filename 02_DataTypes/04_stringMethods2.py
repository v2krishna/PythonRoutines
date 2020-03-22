"""
cont'd of string datatypes
method              >>>> Method Description
endswith(s1;str)    >>>> returns true or false based on the string is ending or not
startswith(s1;str) >>>> returns bool
count(substring)   >>>> returns int number of the occurences of substring in the string
find(s1)           >>>> returns lowers index from where s1 starts in the string.
                        if not found returns -1
rfind(s1)         >>>> returns highest  index from the where s1 starts with the string ;
                if not found retruns -1
"""

str1 = "Welcome to Python"
print(str1.endswith("Python"))
print(str1.startswith("Python"))
print(str1.count("o"))
print(str1.find("Python"))
print(str1.rfind("o"))

