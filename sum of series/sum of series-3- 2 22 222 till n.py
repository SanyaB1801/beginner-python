#WAP to find the sum of the series 2 + 22 + 222 + ….. n terms
n=int(input("Enter no. of terms : "))
s=0
for i in range(n):
    for j in range(i+1):
        s+=2*(10**j)
print("The sum of the series will be ",s)