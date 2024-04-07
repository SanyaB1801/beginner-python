i=0
sum=0
while True:
    n=int(input("Enter no. "))
    sum = sum + n
    i = i + 1
    if n==0:
        break
    avg = sum/i
print("Average of the numbers is: ",avg)