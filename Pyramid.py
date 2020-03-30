n=int(input())
z=n
x=1
while(x<=n):
   for i in range(z-1):
       print(" ",end="")
   y=2*x-1
   for i in range(y):
       print("*",end="")
   for i in range(z-1):
       print(" ",end="")
   print("")
   z=z-1
   x=x+1        

    
