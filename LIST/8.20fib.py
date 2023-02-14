a=0
b=1
n=int(input("Enter the number of terms"))
i=2
list1=[a,b]
while i<n:
    s=a+b
    list1.append(s)
    a=b
    b=s
    i+=1

print(list1)
sum =0
i=0
for i in list1:
    sum+=i
    
print(sum)
