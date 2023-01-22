fhand=open('file.txt','r')
#single line and searching through a file
for chose in fhand:
    chose=chose.rstrip()
    if chose.startswith('I'):
        print(chose)

    #print(chose)

#read whole file
inp=fhand.read()
print(inp)
