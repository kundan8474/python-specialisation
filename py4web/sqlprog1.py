import sqlite3
import re

conn=sqlite3.connect('org.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fhandle=open('mbox.txt')
for lines in fhandle:
    if not lines.startswith('From '):
        continue
#extracting org name
    parts=lines.split()
    email=parts[1]
    spos=email.find('@')
    org=email[spos+1:]
#performming operations on database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('Insert into Counts (org,count) values (?,1)',(org,))
    else:
        cur.execute('Update Counts set count=count+1 where org=?',(org,))
conn.commit()
sqlq='SELECT * FROM Counts Order By count Desc Limit 10'
for i in cur.execute(sqlq):
    print(str(i[0]),i[1])
conn.close()
