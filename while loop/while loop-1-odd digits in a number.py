#WAP to read a number from the user and print the sum of odd digits in a number.
n=int(input("Enter the number: "))
s = 0
while n!=0:
    r = n%10
    if r%2!=0:
        s = s + r
    n//=10
print ("Sum of odd digits = ",s)