#WAP to read a tuple and a searching element and search the particular
#element in the tuple.
t=eval(input("Enter the tuple: "))
c=int(input("Enter searching element: "))
if c in t:
    print("Element is present.")
else:
    print("Element not present.")