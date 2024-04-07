'''
WAP to read an integer list from user
and print sum of all elements
'''
l=eval(input("Enter list: "))
sum=0
for i in l:
    sum+=i
print(sum)