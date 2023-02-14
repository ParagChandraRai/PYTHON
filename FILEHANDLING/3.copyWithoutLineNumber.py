with open('file1.txt', 'r') as input_file:
    with open('file2.txt', 'w') as output_file:
        for line in input_file:
            line_without_number = line.split(' ', 1)[1]
            output_file.write(line_without_number)
