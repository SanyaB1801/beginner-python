#WAP to check if dart hits on the dart or not.
print ("The board has a radius of 10 unit.\n")
x=float(input("Enter the x co-ordinate: "))
y=float(input("Enter the y co-ordinate: "))
if (((x**2)+(y**2))**0.5)<10:
    print ('The dart hit the board.')
else:
    print ('The dart did not hit the board')