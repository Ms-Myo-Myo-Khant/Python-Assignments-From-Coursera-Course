fname = input("Enter file name: ")
fh = open(fname)
count=0
sum=0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    index=line.find('0')
    value=line[index:]
    value=float(value)
    sum=sum+value
    count=count+1
print(sum/count)
print("Average spam confidence:",(sum/count))
