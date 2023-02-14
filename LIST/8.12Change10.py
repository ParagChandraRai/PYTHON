def change(list1):
    for i in range(len(list1)):
        list1[i]=list1[i]*10
    print("After changing in function",list1)

num_list=[1,2,3,4,5]
print("original list",num_list)
change(num_list)
print("list after change",num_list)
