#WAP to read a tuple from the user and print the sum of the even elements.
t=eval(input("Enter a tuple : "))
sum=0
for i in t:
    if i%2==0:
        sum+=i
print(sum)