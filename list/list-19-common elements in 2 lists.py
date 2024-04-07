#WAP to read two lists from the user and check if they have a common element or not
l1=eval(input("Enter first list : "))
l2=eval(input("Enter second list : "))
c=0
common=[]
for i in l1:
    if i in l2:
        c+=1
        common+=[i,]
if c==0:
    print("No common elements were found.")
else:
    print("There were {} common elements. {}".format(c,common))