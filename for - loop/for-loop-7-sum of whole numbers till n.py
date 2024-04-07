#Write a program to print the sum of first n whole numbers,
#where n is the number input by theu ser.
n=int(input("Enter the number: "))
s=0
for i in range(0,n+1):
    s=s+i    
print("Sum = ",s)