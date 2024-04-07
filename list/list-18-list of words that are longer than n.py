#WAP to make list of words that are longer than n from a given text.
s=input("Enter text : ")
n=int(input("Enter maximum length word : "))
l=[]
t=s.split()
for i in t:
    if len(i)>n:
        l+=[i,]
print(l)