#Write a program to generate and print a list except for the first
#5 elements, where the values are square of numbers between 1 and 30
#(both included).
l=[]
for i in range(1,31):
    l+=[i**2,]
while l[0]!=6**2:
    l.remove(l[0])
print(l)