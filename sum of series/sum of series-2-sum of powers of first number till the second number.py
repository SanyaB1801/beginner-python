#WAP to read two numbers from the user and print sum of powers
#of first number till the second number.
x=int(input("x: "))
n=int(input("n: "))
sum=0
for i in range(n+1):
    sum = sum + (x**i)