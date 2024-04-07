#Create a dictionary with the roll number, name, and marks of n students in a class and display the names of students who have marks above 75.
n=int(input("Enter number of students: "))
d={}
for i in range(n):
    rno=int(input("Enter roll no.: "))
    nm=eval(input("Enter name and marks: "))
    #Enter in list form
    d[rno]=nm
print(d)
for rno,nm in d.items():
    if nm[1]>75:
        print(rno,nm)