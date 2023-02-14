num_list=[1,2,3,4,5,6,7,4,2,5]
num=int(input("Enter the value to be searched"))
count=0
i=0
while i<len(num_list):
    if num==num_list[i]:
        print(num ,"found at location ",i)
        count+=1
    i+=1
print(num,"appears",count,"times in the list")
    
