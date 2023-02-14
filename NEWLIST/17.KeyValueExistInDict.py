
my_dict = {'name': 'John', 'age': "25", 'city': 'New York'}

key = input("Enter key: ")
value = input("Enter value: ")
if key in my_dict and my_dict[key] == value:
    print("Key-value pair exists in the dictionary")
else:
    print("Key-value pair does not exist in the dictionary")
