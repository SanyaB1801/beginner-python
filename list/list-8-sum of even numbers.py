#WAP to read a list from the user and print the sum of the even elements
l=eval(input("Enter a list: "))
sum=0
for i in l:
    if i%2==0:
        sum+=i
print(sum)