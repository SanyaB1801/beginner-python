#Q4
'''
Write Python script to create a dictionary with class and the
name of a class teacher and delete a particular class and its
teacher name.
'''
n=int(input("Number of classes: "))
d={}
while n>0:
    cl=input("Enter class: ")
    name=input("Enter name of the teacher: ")
    d[cl]=name
    n-=1
print(d)
i=input("Enter class to be deleted : ")
del d[i]
print(d)

#OR

d= {}
while True:
    k=input("Enter the key")
    teacher=input("Enter the teacher name" )
    d[k]=teacher
    c=input("Wish to continue y\n")
    if c=='n':
        break
print( "Dictionary =", d)
de=input("Enter the key which you want to delete")
if de in d:
    del d[de]
    print( "Data Deleted")
    print("Dictionary : \n", d)
else:
    print("Data does not exist")