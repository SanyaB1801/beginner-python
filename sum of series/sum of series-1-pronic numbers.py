'''
WAP to print all Pronic numbers between 1 to 100
(A number is said to be pronic number if it is a product of two
consecutive numbers.)
For example:
6 = 2 x 3
72 = 8 x 9
Input:
 range(1, 101)
Output:
 Pronic numbers between 1 and 100: 2 6 12 20 30 42 56 72 90
'''
s=0
for i in range(1,101):
    for j in range(i+1):
        if i==j*(j+1):
            print(i,end=' ')
            s+=i
            break
print()
print("Sum of pronic numbers between 1 and 100 is ",s)