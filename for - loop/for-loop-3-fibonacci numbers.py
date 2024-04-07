n=int(input(("Print the first ___ terms of Fibonacci Series.")))
a=0
print(a,end=' ')
b=1
for i in range(1,n):
    print(b,end=' ')
    a,b=b,b+a    #a takes the value of b & b takes the value b+a