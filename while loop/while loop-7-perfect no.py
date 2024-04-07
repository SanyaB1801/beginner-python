#WAP to check if the given no. is perfect no. or not. (eg: 1+2+3=6)
n=int(input("Enter a number: "))
f=0
i=1
while i<=n//2:
    if n%i==0:
        f=f+i
    i = i + 1
if f==n:
    print("It is a perfect number")
else:
    print("It is not a perfect number")