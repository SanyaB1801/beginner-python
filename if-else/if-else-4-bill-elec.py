cname=input("Name: \n")
ad=input("Address: \n")
p=float(input("Previous meter reading: \n"))
c=float(input("Current meter reading: \n"))
nr=c-p
bamount=100

if nr<=200:
    bamount+=nr*3.0
elif nr<=400:
    bamount+=600+(nr-200)*4.50
elif nr<=700:
    bamount+=600+900+(nr-400)*6.50
else:
    bamount+=600+900+1950+(nr-700)*8.50

print("Mr/Ms. {},r/o {}, your bill amount = {}". format(cname, ad, bamount))