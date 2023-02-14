try:
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
except ValueError:
        print("Invalid input! Please enter a valid number.")

result = num1 + num2
print(result)
