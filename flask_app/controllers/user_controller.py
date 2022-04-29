from flask import render_template, request, redirect, session, flash, jsonify

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User
from flask_app.models.vehicle import Vehicle

### BASE ROUTE
@app.route('/')
def index():

    return redirect ('/zeronow')

@app.route('/zeronow')
def homepage():

    return render_template ('login.html')

### VALIDATE REGISTER ROUTE
@app.route('/register', methods=['POST'])
def register_user():

    query_data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        'password': request.form['password'],
        'confirm_password' : request.form['confirm_password']
    }

    if User.validate_registration(query_data):
        pw_hash = bcrypt.generate_password_hash(query_data['password'])
        query_data['password'] = pw_hash
        del query_data['confirm_password']
        new_user_id = User.register_user (query_data)
        session['user_id'] = new_user_id
        return redirect ('/zeronow/dashboard')

    return redirect('/zeronow/dashboard')

### PROCESS LOGIN ROUTE

@app.route('/login', methods=['POST'])
def login():

    data = {
        'email' : request.form['email']
    }
    user_in_db = User.get_by_email(data)
    
    if not user_in_db:
        flash ('Invalid Email or Password')
        return redirect ('/')

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash ('Invalid Email or Password')
        return redirect ('/')

    # if given pw matches password in db, log user in and set user_id into session
    session['user_id'] = user_in_db.id

    return redirect ('/zeronow/dashboard')

@app.route('/zeronow/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please register or login to use Zero Now!')
        
    query_data = {
        'user_id' : session['user_id']
    }
    user = User.get_by_id(query_data)
    vehicles = Vehicle.get_user_vehicles()
    
    return render_template('dashboard.html', user = user, vehicles = vehicles)

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/zeronow')