#WAP to create a list by concatenating a given list which range goes from 1 to n.
l=eval(input("Enter list : "))
n=int(input("n : "))
new=[]
for i in range(1,n+1):
    for a in l:
        new+=[a+str(i),]
print(new)