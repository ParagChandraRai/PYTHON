def convert(x):
    return ord(x)

chr_list=['a','b','c','d','e']
print("Corresponding ASCII Value")
new_list=list(map(convert,chr_list))
print(new_list)
