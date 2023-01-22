count=0
tot=0.0
while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print('Invail Input')
        continue
    #print(fval)
    count=count+1
    tot=tot+fval
#print('All Done')
print(tot,count,tot/count)
