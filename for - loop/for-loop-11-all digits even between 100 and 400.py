#WAP to find numbers b/w 100 and 400 where each digit of a number is even
c=0
for i in range(100,401):
    s=str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        print(s,end=', ')
        c+=1
print()
print("The condition is satisfied by",c,"numbers between 100 and 400.")