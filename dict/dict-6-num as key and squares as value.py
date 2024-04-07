#WAP to print a dictionary the keys are numbers between 2 numbers and
#the values are square of keys.
d={}
l=int(input("Enter minimum limit : "))
u=int(input("Enter maximum limit : "))
for i in range(l,u+1):
    d[i]=i**2
print(d)