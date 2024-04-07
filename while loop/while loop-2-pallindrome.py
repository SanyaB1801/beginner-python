#WAP to read a number from the user and check if it is pallinndrome or not (eg: 12321)
n=int (input ("Enter the number: ") )
rev=0
org=n
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n//=10
if org==rev:
    print("It is palindrome")
else:
    print("Not palindrome")