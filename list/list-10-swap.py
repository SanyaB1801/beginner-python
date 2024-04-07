'''
Input a list of numbers and swap elements at the even location
with the elements at the odd location.
'''
l=eval (input("Enter the list") )
for i in range(len(l)) :
    if i%2==0:
        l[i], l [i+1]=l[i+1], l[i]
print(l)