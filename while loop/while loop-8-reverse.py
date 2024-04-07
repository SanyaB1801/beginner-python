#WAP to read a number from the user and print its reverse.
n=int (input ("Enter number ") )
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n//=10
print("Revese digits", rev)