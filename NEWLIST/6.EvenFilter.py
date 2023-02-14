def check(x):
    if x%2==0:
        return 1
    else:
        return 0

#num_list=[1,2,3,4,5,6]
n_list=list(filter(check,range(2,50)))
print(n_list)
