import functools
def add(x,y):
    return x+y
num_list=[1,2,3,4,5,6,7,8,9,10]
print("Sum of 1 to 10 Natural No")
print(functools.reduce(add,num_list))
