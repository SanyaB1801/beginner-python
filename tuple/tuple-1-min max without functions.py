#WAP to read the tuple from the user and print the max and min element
#without using functions.
t=eval(input("Enter the numbers: "))
mx=mn=0
for i in t:
    if i<mn:
        mn=i
    elif i>mx:
        mx=i
print("Max = ",mx)
print("Min = ",mn)