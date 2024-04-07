#WAP to find Armstrong no. b/w given range
l=int(input("Lower limit: "))
u=int(input("Upper limit: "))
for n in range(l,u+1):
    sum=0
    x=n
    while x>0:
        digit=x%10
        sum=sum+digit**3
        x=x//10
    if sum==n:
        print(n, end=' ')