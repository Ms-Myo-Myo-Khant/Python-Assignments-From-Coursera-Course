def computepay(h,r):
    if h<=40:
        return h*r
    elif h>40:
        return (40*r)+(1.5*r*(h-40))

hrs=input("Enter Hours:")
rate=input("Enter Rate:")

hr=float(hrs)
ra=float(rate)

p=computepay(hr,ra)
print("Pay",p)
