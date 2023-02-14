my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 3}


max_value = 0
min_value = 999

for key, value in my_dict.items():
    if value > max_value:
        max_value = value
        max_key = key
    if value < min_value:
        min_value = value
        min_key = key


print("Maximum value:", max_value, "with key:", max_key)
print("Minimum value:", min_value, "with key:", min_key)
