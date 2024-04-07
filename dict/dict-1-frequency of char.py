#WAP to create a dictionary using frequency of a character in a string.
s = input("Enter a string: ")
d = {}
for i in s:
    if i in d:
        d[i]= d[i] + 1
    else:
        d[i] = 1
print(d)