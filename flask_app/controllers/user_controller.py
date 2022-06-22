from flask import render_template, session, redirect, request, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

from flask_app import app

bcrypt = Bcrypt(app)

@app.route('/')
@app.route('/login')
def display_form():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def user_login():
    if User.validate_login(request.form) == False:
        return redirect('/login')
    else:
        result = User.get_one(request.form)
    
    if result == None:
        flash("Wrong credentials""error_login")
        return redirect('/login')
    else:
        session['first_name'] = result.first_name
        session['last_name'] = result.last_name
        session['email'] = result.email
        session['user_pass'] = result.user_pass
        return redirect('/welcome')
    
@app.route("/account/new")
def create_new_account():
    if User.validate_registration(request.form) == False:
        return redirect('/login')
    else:
        data = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "user_pass" : bcrypt.generate_password_hash(request.form['user_pass'])
        }
        user_id = User.create(data)
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        session[id] = user_id
        return redirect("/welcome")

@app.route("/welcome")
def login_success():
    return render_template("welcome.html" first_name = first_name)