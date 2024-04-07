print("There is a qudratic equation of the form ax^2 + bx + c, \n")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
D=(b**2)-(4*a*c)
if D>0:
    print("The roots are real & unequal.")
elif D==0:
    print("The roots are real & equal.")
else:
    print("The roots are not real.")
n1=(-b + (D)**(1/2))/(2*a)
n2=(-b - (D)**(1/2))/(2*a)
print("The roots are ",n1," and ",n2)