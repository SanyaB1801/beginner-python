#Q1 NCERT
#WAP to read some text from the user and give count of alphabets, special characters,
#digits, and words. Also give count of total characters.
s=input("Enter text: ")
c=al=dig=sp=w=0
for i in s:
    c+=1
    if i.isalpha():
        al+=1
    elif i.isdigit():
        dig+=1
    elif i.isspace():
        w+=1
    else:
        sp+=1
s=s.split()
print("Alphabet = ",al)
print("Special characters = ",sp)
print("Digits = ",dig)
print("Words = ",w)
print("Total = ",c)