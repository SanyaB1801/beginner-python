l=[1,2,3,4,5,6,8,5,3,6,4,4,5,6,4,3,2]
l=eval(input("Enter list : "))
l=l[::-1]
l.sort()
print(l)
l.sort(reverse=True)
print(l)