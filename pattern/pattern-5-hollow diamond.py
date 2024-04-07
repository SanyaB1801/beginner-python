# Python program to print a hollow
# diamond pattern
k = 0
n=6
# Print upper triangle
for i in range(1, n+1):#no. of rows
# Print spaces
    for j in range(1, n-i+1):
        print(" ", end="")
# Print
    while (k!= (2*i - 1)):
        if (k == 0 or k == 2 * i - 2):
            print ("*", end="")
        else:
            print (" ", end="")
        k=k+1
    k = 0
    # move to next row
    print(""),
n = n - 1
# Print Lower triangle
for i in range (n, 0, -1):
#print spaces
    for j in range(0,n-i+1):
        print(" ",end='')
    #print #
    k = 0
    while (k!=(2*i-1)):
        if k==0 or k==2*i-2:
            print("*",end='')
        else:
            print(' ',end='')
        k=k+1
    print('')