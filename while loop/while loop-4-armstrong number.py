#Armstrong number (e.g. 1^3 + 5^3 + 3^3 =153 or 407 = 4^3 + 0^3 + 7^3)
n=int (input("Enter number "))
a=0
org=n
while n!=0:
    r=n%10
    a+=r**3
    n//=10
if org==a:
    print("It is Armstrong number.")
else:
    print( "It is not Armstrong number.")