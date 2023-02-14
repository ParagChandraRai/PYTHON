def square2(x):
     return x**2

squares=[]
squares=list(map(square2,range(1,11)))
print("List of squares in the range 1-10 ",squares)
sum=0
for i in squares:
    sum+=i
print("Sum of squares in the range 1-10=",sum)
    
