str=input()
j=0
for i in range(0,len(str)):
    
    if i%2==0:
        print(str[j].upper(),end="")
    else:
        print(str[j].lower(),end="")
    
    j=j+1    
