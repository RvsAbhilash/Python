l=int(input())
b=int(input())
i=1

for j in range(l):
    print("*",end="")
print("")  
    
b=b-2
while(b!=0):
    print("*",end="")
    for i in range(l-2):
        print(" ",end="")
    print("*",end="")
    print("")
    b=b-1
for j in range(l):
    print("*",end="")
print("")    
