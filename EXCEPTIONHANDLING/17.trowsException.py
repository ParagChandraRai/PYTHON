import math
def find_square_root(num):
    if num < 0:
        raise ValueError("The number must be positive")
    return math.sqrt(num)

try:
    num = float(input("Enter a positive number: "))
    square_root = find_square_root(num)
    print(square_root)
except ValueError as ve:
    print(ve)
