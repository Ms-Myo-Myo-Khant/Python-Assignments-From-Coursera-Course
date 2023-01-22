fname = input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
    line=line.split()
    for w in line:
        if w in lst:continue
        lst.append(w)

lst.sort()
print(lst)
