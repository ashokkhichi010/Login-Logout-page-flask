import sqlite3 as sql

database='userDataBase.db'
conn=sql.connect(database)
curs=conn.cursor()
curs.execute("SELECT * FROM users")
user=curs.fetchall()
curs.execute('')
conn.close()
            
for i in user :
    uid=i[0]
    fname=i[1]
    lname=i[2]
    user=i[3]
    password=i[4]
    print(uid,fname,lname,user,password)
