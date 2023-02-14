try:
    x = 1/3
    y = int("abc")
    z = [1,2,3]
    print(z[4])
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid value")
except IndexError:
    print("Index out of range")
except Exception as e:
    print("An unexpected error occurred:", e)
