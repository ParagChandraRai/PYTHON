n_list=[5,12,8,9,3,4,5,1]
i=len(n_list)//2
max=0
while i<len(n_list):
    if n_list[i]>max:
        max=n_list[i]
    i+=1
print(max)
