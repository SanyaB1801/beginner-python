#WAP to calculate a dog's age in dog's years.
#Note: For the first two years, a dog year is equal to 10.5 human years.
#After that, each dog year equals 4 human years.
a=int(input("Enter the dog's age : "))
if a<3:
    dy=a*10
else:
    dy=2*10.5
    for i in range(a-2):
        dy+=4
print("Age of dog in dog's years is",dy)