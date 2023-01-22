fname=input('Enter the filename: ')


 
try:
    fhand=open(fname)
except:
    print('File cannot be opened:',fname)
    quit()


count=0
for line in fhand:
    line=line.rstrip()
    print(line)
    if line.startswith('I'):
         count=count+1
print('\n\nThere were ',count,' subject lines in ',fname)
