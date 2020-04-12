"""
Search the element in the list if match print element found else "not found"
"""
list_1 = [10, 20, 30, 40, 50]
search = int(input("Enter the searchable element:"))
for element in list_1:
    if element == search:
        print("Element found in the list")
        break
else:
    print("element not found")