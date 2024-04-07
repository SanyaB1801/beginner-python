#Write a program to find numbers in a range which are divisible by n.
l=int(input("Enter lower limit : "))
u=int(input("Enter upper limit : "))
n=int(input("Enter divisor : "))
for i in range(l,u+1):
    if i%n==0:
        print(i,"is divisible by",n)