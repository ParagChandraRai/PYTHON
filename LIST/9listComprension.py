def print_consonant(mystring):
    vowels=["a","e","i","o","u"]
    # creating a list using list comprehension
    mylist = [ item for item in mystring if item not in vowels]   
    for item in mylist:
        print(item)
        
print_consonant("Rajkumar") 
