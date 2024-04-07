# pattern 1--increasing abc triangle with length=alphabetnum
x = 65
for i in range (1,7):
    x=65
    for j in range (1,i+1):
        print(chr(x),end=' ')
        x=x+1
    print()