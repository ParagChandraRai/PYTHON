import random
num_list=[]
for i in range(10):
    val=random.randint(1,100)
    num_list.append(val)
print("original list: ",num_list)
even_list=[]
odd_list=[]
for i in range(len(num_list)):
    if(num_list[i]%2==0):
        even_list.append(num_list[i])
    else:
        odd_list.append(num_list[i])
print("Even number list: ",even_list)
print("odd number list: ",odd_list)

