import os
file1=open("file1.txt","r")
file2=open("file2.txt","r")

text1=file1.read()
text2=file2.read()
file1.close()
file2.close()

file1=open("file1.txt","w")
file2=open("file2.txt","w")
file1.write(text2)
file2.write(text1)

file1.close()
file2.close()
