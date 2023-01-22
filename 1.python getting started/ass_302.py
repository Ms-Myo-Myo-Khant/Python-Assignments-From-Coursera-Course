hrs=input("Enter Hours: ")
rate=input("Enter Rate: ")
try:
    h=float(hrs)
    r=float(rate)
except:
    print("Error,please enter numeric input:")
    quit()

if h<=40:
    pay=h*r
    print(pay)

else:

    pay=(40*r)+(r*1.5*(h-40))
    print(pay)
