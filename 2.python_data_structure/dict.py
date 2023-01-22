fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
mail=dict()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '):continue
    words=line.split()
    mail[words[1]]=mail.get(words[1],0)+1

bigcount=None
bigword=None
for word,count in mail.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
