#WAP to print an AP given first term, common difference and maximum limit.
a=int(input("Enter first term: "))
d=int(input("Enter common difference: "))
l=int(input("Enter maximum limit: "))
while a<=l:
    print (a, end=' ')
    a+=d