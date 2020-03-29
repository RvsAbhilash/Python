a=input()
l=len(a)
sum=0
n=int(a)
while(n!=0):
    d=n%10
    sum=sum + d**l
    n=n//10
print(sum)    
