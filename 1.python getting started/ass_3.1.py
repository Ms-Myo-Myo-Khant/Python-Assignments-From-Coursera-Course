hrs=input("Enter Hours: ")
rate=input("Enter Rate: ")
h=float(hrs)
r=float(rate)

if h<=40:
    pay=h*r
    print(pay)

else:

    pay=(40*r)+(r*1.5*(h-40))
    print(pay)
