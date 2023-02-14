def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i, (line1, line2) in enumerate(zip(lines1, lines2)):
            if line1 != line2:
                print(f'Line {i + 1} is different:')
                print(f'File 1: {line1.strip()}')
                print(f'File 2: {line2.strip()}')

file1 = 'file1.txt'
file2 = 'file2.txt'
compare_files(file1, file2)
