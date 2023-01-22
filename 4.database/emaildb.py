import sqlite3  #to get library

conn = sqlite3.connect('emaildb.sqlite')#connection #emaildb is creating sqlite database file
                                        #if  emaildb doesn't exist,it will create when it run
cur = conn.cursor()#like handle,open it and send sql cmd and retrieve data

cur.execute('DROP TABLE IF EXISTS Counts')#drop table Counts if exist.

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')#create table.

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1] #take email address

    #database exection start
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))#?=using placeholder
    row = cur.fetchone()#grab first one from select.

    #email is first time
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    #email is already exist.
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()#write to disk each time
#conn.commit()-->can write all data to disk after loop
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'#by descending get top 10

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])#0-email,1-count

cur.close()
