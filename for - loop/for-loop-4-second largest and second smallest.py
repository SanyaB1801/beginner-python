#WAP to read n number from user and print second largest and second smallest no.
n = int(input("No. of numbers to be entered : "))
l1=l2=0
s1=s2=5000000
for i in range(1,n+1):
    x=int(input('Enter a number :'))
    if x>l1:
        l2=l1
        l1=x
    elif x>l2 and l2<l1:
        l2=x
        
    if x<s1:
        s2=s1
        s1=x
    elif x<s2 and s2>s1:
        s2=x
print('Largest is ',l1,' and second largest is ',l2)
print('Smallest is ',s1,' and second smallest is ',s2)