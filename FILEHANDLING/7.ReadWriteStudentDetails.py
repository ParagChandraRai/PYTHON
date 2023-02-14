def write_student_details(name, age, course):
    with open("student_details.txt", "w") as file:
        file.write("Name: " + name + "\n")
        file.write("Age: " + str(age) + "\n")
        file.write("Course: " + course + "\n")

def read_student_details():
    with open("student_details.txt", "r") as file:
        for line in file:
            print(line, end="")

name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
course = input("Enter student's course: ")

write_student_details(name, age, course)
print("\nStudent details:")
read_student_details()
