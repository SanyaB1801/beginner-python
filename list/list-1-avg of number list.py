#WAP to read an integer list from the user and print the avg
#of the elements

l=eval(input("Enter a list: "))
s=0
for i in l:
    s+=i
avg=s/len(l)
print(avg)