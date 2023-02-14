def count_records(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

filename = 'file1.txt'
records = count_records(filename)
print(records)
