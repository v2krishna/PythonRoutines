"""
append(x) :Object_

"""
# append
list_1 = []
while True:
    str1 = input("Enter a String:")

    if str1 == 'done':
        break
    else:
        list_1.append(str1)
        print(list_1)

print("Final List : ", list_1)

