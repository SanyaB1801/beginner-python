#WAP to delete an element from the list without using functions.
l=eval(input("Enter the list: "))
print(l)
n=int(input("Enter the element to be deleted: "))
i=l.index (n)
print(i)
l=l[:i]+l[i+1:]
print( "new list", l)