from flask import Flask,render_template,redirect,request,url_for,session
from models import Users

app=Flask(__name__)
app.secretkey="2480"

@app.route('/')
def home:
    return redirect(url_for('login'))

@app.route('/register' methods= 'POST','GET')
def register:
    if request.method =='POST':
        username=request.form['username']
        password=rqusest.form['password']

        if not username or not password:
            error=f"<hi>All fields are required.<h1>"
        else:
            db.session()
            try:
                existing_user=db.query(Users).filer_by(username=username).first()
                if existing_user:
                    error=f"<h1>User already exists<h1>"
                else:
                    new_user=User(username=username,password=password)
                    db.add(new_user)
                    db.commit()

                    return redirect(url_for('login')) 
                finally:
                    db.close()     

@app.route('/login' methods='GET')
def login:
    if request.method =='GET':
        username=request.form['username']
        password=rqusest.form['password']

        if not username or not password:
            error=f"<hi>Invalid credentials<h1>"
        else:
            db.session()
            try:
                user = db.query(Users).filter_by(username=username).first()
                if user in session :
                    session ['username']=user
                    session['user_id']=user.id
                    return redirect(url_for('user.html'))

            finally:
                db.close()             




