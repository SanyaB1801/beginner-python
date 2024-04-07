m=eval(input("Enter marks in maths: "))
p=eval(input("Enter marks in physics: "))
c=eval(input("Enter marks in chemistry: "))
t=p+c+m
if m>=65 and p>=55 and c>=50 and t>=180:
    print("You are eligible.")
else:
    print("You are not eligible.")