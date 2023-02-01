l=[1,2,3,45,6,7,8,9,10]
s=0
i=0
print(len(l))
while i<len(l):
    if l[i]%2==0:
        s+=l[i]
    i+=1

print(s)
