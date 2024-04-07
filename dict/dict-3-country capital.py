'''
Write Python script to input country name and its capital of
5 countries. Add them to a dictionary and also display it.
'''
n=5
d={}
while n>0:
    country=input("Enter country: ")
    capital=input("Enter capital of the country: ")
    d[country]=capital
    n-=1
print(d)

#OR

for i in range(5):
    country=input("Enter country: ")
    capital=input("Enter capital of the country: ")
    d[country]=capital
    n-=1
print(d)