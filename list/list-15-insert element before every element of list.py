#WAP to insert an element before each element of a list.
l=eval(input("Enter list : "))
c=input("Enter element : ")
new=[]
for i in l:
    new+=[c,i,]
print("New list : ",new)