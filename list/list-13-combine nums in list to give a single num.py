#WAP to convert a list of multiple integers into a single integer.
'''
Sample list: [11, 33, 50]
Expected Output: 113350
'''
l=eval(input("Enter list : "))
s=0
for a in l:
    s+=a
    if a==l[-1]:
        break
    else:
        s*=10**len(str(a))
print(s)