m=eval(input("Marks: "))
if m<25:
    g='F'
elif m<=45:
    g='E'
elif m<=50:
    g='D'
elif m<=60:
    g='C'
elif m<=80:
    g='B'
elif m<=100:
    g='A'
else:
    g='Marks invalid'
    
print("Grade = ",g)