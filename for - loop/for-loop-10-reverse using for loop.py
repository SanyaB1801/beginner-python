#WAP to read a word from the user and reverse it.
w=input("Enter the word : ")
new=''
for i in range(1,len(w)+1):
    new+=w[len(w)-i]
print(new)