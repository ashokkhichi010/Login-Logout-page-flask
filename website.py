from flask import Flask,redirect,render_template, request
import sqlite3 as sql

'   creating environment for flask :'# > py -m venv envName
'   activating environmet for flask:'# > envName\Scripts\activate
'   installing flask                '# > pip install flask
'   updating flask                  '# > python.exe -m pip install --upgrade pip
#   now you can write progrrames in flask

def InsertIntoTable(Fname,Lname,username,password):
    database='userDataBase.db'
    conn=sql.connect(database)
    curs=conn.cursor()
    U='INSERT INTO users(Fname,Lname,username,password)'
    V=str(' VALUES'+str((Fname,Lname,username,password)))
    print(V)
    myqurry=str(U+V)
    print(myqurry)
    curs.execute(myqurry)
    conn.commit()
    conn.close()

global log
global sign

log=sign=0

app=Flask(__name__)
########################################################
@app.route('/')
def index():
    return render_template('index.html')
########################################################
@app.route('/login',methods=['post','get'])
def login():
    global log
    global sign
    if log==0:
        sign=0
        log=1
        return render_template('/login.html',log=0)
    uname = request.form.get('uname')
    passw = request.form.get('pass')
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
        if uname==user and passw==password:
            log=0
            return render_template('profile.html',uid=uid,fname=fname,lname=lname,user=user,passw=password)
    else:
        msg='!  username  or  password  invalide  !'
        return render_template('login.html',msg=msg,log=log)
########################################################
@app.route('/signup',methods=['post','get'])
def signup():
    global sign
    global log
    if sign==0:
        sign=1
        log=0
        return render_template('/signup.html')
    fn=request.form.get('fname')
    ln=request.form.get('lname')
    un=request.form.get('uname')
    pw=request.form.get('pass')
    database='userDataBase.db'
    if fn==None or ln==None or un==None or pw==None:
        msg = '!  Please  !'
        sign=1
        return render_template('signup.html',msg=msg,sign=sign)
    conn=sql.connect(database)
    curs=conn.cursor()
    curs.execute("SELECT * FROM users")
    user=curs.fetchall()
    curs.execute('')
    conn.close()

    for i in user :
        if un==i[3]:
            msg = str(i[3]+'  already registered  ! please change your user name !')
            sign=1
            return render_template('signup.html',msg=msg,sign=sign)
    InsertIntoTable(fn,ln,un,pw)
    log=0
    sign=0
    return redirect('/login')
########################################################
@app.route('/logout')
def logout():
    global log
    log=0
    return redirect('/login')
########################################################
@app.route('/profile',methods=['post','get'])
def profile():
    pass
########################################################
if __name__=='__main__':
    app.run( debug = True )







#C:\NewFlaskProject>venv\Scripts\activate

#(venv) C:\NewFlaskProject>set FLASK_APP=website.py

#(venv) C:\NewFlaskProject>set FLASK_ENV=development

#(venv) C:\NewFlaskProject>flask run --host=0.0.0.0
# * Serving Flask app 'website.py' (lazy loading)
# * Environment: development
# * Debug mode: on
# * Running on all addresses (0.0.0.0)
#   WARNING: This is a development server. Do not use it in a production deployment.
# * Running on http://127.0.0.1:5000
# * Running on http://192.168.1.11:5000 (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 803-456-437
