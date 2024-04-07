'''
Write a program to read email IDs of n number of
students and store them in a tuple. Create two new
tuples, one to store only the usernames from the
email IDs and second to store domain names from
the email ids. Print all three tuples at the end of the
program. [Hint: You may use the function split()]
'''
n=int(input("n = "))
efinal=()
dfinal=()
complete=()
for i in range(n):
    email=input("Enter the email id: ")
    complete=complete+(email,)
    em,dm=email.split('@')
    efinal=efinal+(em,)
    dfinal=dfinal+(dm,)
print("Email id =",efinal)
print('Domain name =',dfinal)
print('complete =',complete)