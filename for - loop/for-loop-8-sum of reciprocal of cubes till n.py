#WAP to find the sum of 1 + 1/8 + 1/27 + ...... + 1/n3,
#where n is the number input by the user.
n=int(input("Enter value of n : "))
s=0
for i in range(1,n+1):
    s+=1/(i**3)
print("Sum of 1 + 1/8 + 1/27 + ...... + 1/({}^3) = {}".format(n,s))
