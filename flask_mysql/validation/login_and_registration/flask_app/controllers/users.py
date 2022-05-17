from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/user', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash
    }

    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {"email" : request.form['email']}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash(u"Invalid Email/Password", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash(u"Invalid Email/Password", "login")
        return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash(u"You must be logged in to view the dashboard", "login")
        return redirect('/')

    data = {
        'id' : session['user_id']
    }

    user = User.get_by_id(data)
    print(user)
    return render_template("dashboard.html", user = user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')