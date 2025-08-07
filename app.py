from flask import Flask, render_template, redirect, request, url_for, session
from models import Users ,Admins ,Products
from connection import SessionLocal

app = Flask(__name__)
app.secret_key = "2480"

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    success= None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        secondname = request.form['secondname']
        email = request.form['email']

        if not username or not password:
            error = "All fields are required."
        else:
            db = SessionLocal()
            try:
                existing_user = db.query(Users).filter_by(username=username).first()
                if existing_user:
                    error = "User already exists"
                else:
                    new_user = Users(username=username, password=password ,firstname=firstname,secondname=secondname,email=email)
                    db.add(new_user)
                    db.commit()
                    success="Registration Sucessfull"
                    return redirect(url_for('login'))
                   
            finally:
                db.close()
    return render_template('register.html', error=error )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    success= None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            error = "Fill all fields"
        else:
            db = SessionLocal()
            try:
                user = db.query(Users).filter_by(username=username, password=password).first()
                if user:
                    session['username'] = user.username
                    session['user_id'] = user.id
                    success ="Login Sucessfull"
                    return redirect(url_for('dashboard'))
                    
                else:
                    error = "Invalid input."
            finally:
                db.close()
    return render_template('login.html', error=error)


@app.route('/admin login', methods=['GET', 'POST'])
def  adminLogin():
    error = None
    success= None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            error = "Fill all fields"
        else:
            db = SessionLocal()
            try:
                user = db.query(Admins).filter_by(username=username, password=password).first()
                if user:
                    session['username'] = user.username
                    session['user_id'] = user.id
                    success ="Login Sucessfull"
                    return redirect(url_for('adminDashboard'))
                    
                else:
                    error = "Invalid input."
            finally:
                db.close()
    return render_template('admin login.html', error=error)    

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    db = SessionLocal()

    products = db.query(Products).all()
    return render_template('dashboard.html',products=products)

@app.route('/ admin dashboard', methods= ['POST','GET'])
def adminDashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    db = SessionLocal()    

    products = db.query(Products).all()
    return render_template('dashboard.html',products=products)

    error = None
    success= None
    if request.method == 'POST':
        product = request.form['product']
        price = request.form['price']
        stock = 'stock' in request.form
        quantity= request.form['quantity']

        if not product or not price or not stock :
            error = "All fields are required."
        else:
            db = SessionLocal()
            try:
                existing_user = db.query(Products).filter_by(product=product).first()
                if existing_user:
                    error = "Product already exists"
                else:
                    new_user = Products(product=product, price=price ,stock=stock,quantity=quantity)
                    db.add(new_user)
                    db.commit()  
                    return redirect (url_for('adminDashboard'))       
            finally:
                db.close()
    return render_template('admin dashboard.html', error=error )
    
@app.route('/edit_or_delete/<int:product_id>')
def edit_or_delete(product_id):
    pass    


@app.route('/logout')
def logout():
    session.clear()  
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
