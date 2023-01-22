import re
numlist=list()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()
    str=re.findall('([0-9]+)',line)
    if len(str)<1: continue
    length=len(str)
    print(length)
    for i in range(length):
        number=int(str[i])
        print(number)
        numlist.append(number)

print('Sum :',sum(numlist))
