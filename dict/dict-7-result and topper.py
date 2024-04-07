#Write a program to read the name and of marks for n students and
#display the result of all the students and find the topper amongst them.
n=int(input("Enter number of students: "))
d={}
for i in range(n):
    name=input("Enter name of student : ")
    marks=int(input("Enter marks of student : "))
    d[name]=marks
print(d)
l=0
for i in d:
    if d[i]>l:
        l=d[i]
        top=i
print(top,"is the topper.")
