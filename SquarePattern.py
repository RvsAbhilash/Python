n=int(input())
x=1
while(x<=n):
    if x==1 or x==n:
        for i in range(n):
            print("*",end="")
            
    else:
        print("*",end="")
        for i in range(n-2):
            print(" ",end="")
        print("*",end="")
    print("")    
    x=x+1
