"""
Display 1 to 100 in 10 rows in formatting way
"""
for i in range(1,11):
    for j in range(1,11):
        print('{:8}'.format(i *j), end = "")
    print()
print("End of the program")