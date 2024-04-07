#WAP to check if a given no. is prime or not.
n=int(input("Enter a number: "))
if n>1:
    for i in range(2,n//2):
        if n%i==0:
            print("Not prime number.")
            break
    else:
        print("Prime number.")