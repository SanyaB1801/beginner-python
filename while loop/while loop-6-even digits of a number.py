#no. of even digits
n=int(input("Enter the number: "))
c = 0
while n!=0:
    r = n%10
    if r%2==0:
        c = c + 1
    n//=10
print ("Even digits = ",c)