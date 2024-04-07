#WAP to read a list from the user and a searching element and search
#the element using linear search technique.
l=eval(input("enter the list "))
ch=eval(input("enter the character :"))
c=0
for i in l:
    c+=1
    if i==ch:
        print("found {} at {}th place".format(ch,c))
        break
else:
    print(ch," is not in ",l)