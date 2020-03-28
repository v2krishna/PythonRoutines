list_1= [ x for x in range(10)]
print(list_1)
list_1 = [x+1 for x in range(20)]
print(list_1)

# even numbers
list_1 = [x for x in range(40) if x % 2 == 0]
print(list_1)

# odd numbers
list_1 = [x for x in range(50) if x % 2 !=0]
print(list_1)