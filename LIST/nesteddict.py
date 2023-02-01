employee = {'Name': 'John Doe', 'Designation': 'Manager', 'Department': 'Sales',
            'Contact': {'Email': 'johndoe@company.com', 'Phone': '1234567890'}}

print(f"Name: {employee['Name']}")
print(f"Designation: {employee['Designation']}")
print(f"Department: {employee['Department']}")
print(f"Email: {employee['Contact']['Email']}")
print(f"Phone: {employee['Contact']['Phone']}")
