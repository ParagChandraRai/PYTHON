# [‘1a’, ‘2a’, ’3a’, ’4a’]
a = [f"{i}a" for i in range(1,5)]
print(a)
# [‘ab’, ‘ac’, ‘ad’, ‘bb’, ‘bc’, ‘bd’]
b = [f"{i}{j}" for i in "ab" for j in "cd"]
print(b)
# [‘ab’, ‘ad’, ‘bc’]
c = [x for x in b if x[1] in "ad"]
print(c)
# Multiples of 10
d = [x for x in range(0,101,10)]
print(d)
