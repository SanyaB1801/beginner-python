#WAP to read a list and convert the list by half the even element and
#thrice the odd element.
l=eval(input("Enter a list: "))
for i in range(len(l)):
    if l[i]%2==0:
        l[i]=l[i]/2
    else:
        l[i]=3*l[i]
print(l)