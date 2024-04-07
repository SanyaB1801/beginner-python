'''
Write Python script to create a dictionary with famous
monuments and their location. Input name of any monument
and check whether that monument is present in the dictionary
or not. If the monument is not present in the dictionary then
add it to the dictionary.
'''
d = {}
while True:
    k=input("Enter monument: ")
    loc=input("Enter location: " )
    d[k]=loc
    c=input("Wish to continue y/n: ")
    if c=='n':
        break
while True:
    print("Dictionary =", d)
    m = input("Enter a monument: ")
    if m in d:
        print(m,"in dictionary.")
    else:
        l=input("Enter its location : ")
        d[m]=l
    print(d)
    c1=input("Wish to continue y/n: ")
    if c1=='n':
        break