str="X-DSPAM-Confidence: 0.8475"
pos=str.find(':')
#print(pos)
piece=str[pos+2:]
value=float(piece)
print(value,type(value))
