filename=input("Enter the filename")
with open(filename) as file:
    text=file.read()
    tab=0
    space=0
    newline=0
    for char in text:
        if char =='\t':
            tab+=1
        if char ==' ':
            space+=1
        if char =='\n':
            newline+=1


print("TABS:",tab)
print("Spaces:",space)
print("New Lines:",newline)
