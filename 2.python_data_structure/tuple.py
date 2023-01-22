fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
day=dict()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '):continue
    words=line.split()
    date=words[5].split(':')
    day[date[0]]=day.get(date[0],0)+1


for k,v in sorted(day.items()):
    print(k,v)    
