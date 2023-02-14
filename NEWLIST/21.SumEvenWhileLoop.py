num_list=[4,2,3,4]
sum=0
i=0
while i<len(num_list):
    if num_list[i]%2==0:
        sum+=num_list[i]
    i+=1

print(sum)
