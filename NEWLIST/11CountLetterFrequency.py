string = input("Enter a string: ")
letter_frequency = {}

for letter in string:
    if letter in letter_frequency:
        letter_frequency[letter] += 1
    else:
        letter_frequency[letter] = 1

for letter in sorted(letter_frequency.keys()):
    print(letter,letter_frequency[letter])

