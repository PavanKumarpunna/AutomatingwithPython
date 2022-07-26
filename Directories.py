import os
import sys

print(os.getcwd())

os.chdir("E:/")
print(os.getcwd())

for l in os.listdir():
    print(l)
    if "New Text Document.txt"  == l:
        print("File is available")
        f = open(l,"a") #a-append,x-create,r-read,w-write
        f.write("Learning Python")
        print(os.getpid())
        f.close()

    #print(os.getpid())