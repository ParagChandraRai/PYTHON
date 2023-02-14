name = input("Enter your name: ")
try:
    if name == "Rahul":
        raise Exception("Rahul is not allowed.")
    print("Hello " + name)
except Exception as e:
    print(e)
    print("Please quit the program.")
