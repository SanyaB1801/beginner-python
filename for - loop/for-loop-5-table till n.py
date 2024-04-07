#WAP to read a number from the user and print the table upto 10 for each number b/w 2 to user-entered number
n = int(input("n = "))
for i in range (2,n+1):
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))
    print()