# Inspired by COMP3310 Wk10 Task

from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, db_users
from .user import User
import re

auth = Blueprint('auth', __name__)

# Page routes
@auth.route('/login')
def login():
    # Login page route
    return render_template('login.html')
@auth.route('/signup')
def signup():
    # Signup page route
    return render_template('signup.html')

# ---------------------------------------------------------------------------------------------------

@auth.route('/login', methods=['POST'])
def login_post():
    # Gets the email/username field and checks whether it 
    # is an email (contains @###.com) or a username
    email = "email"
    username = "user"

    # Gets password from field
    password = ""

    if not email:
        user == User.query.filter_by(username == username).first()
    elif not user:
        user == User.query.filter_by(email == email).first()
    else:
        user == User.query.filter_by(email == email, username == username).first() 

    if not user or not (user.password == password):
        flash("Invalid login, please try again.")
        current_app.logger.warning("Failed user login attempt")
        return redirect(url_for('auth.login'))
    
    login_user(user)
    flash("Logged in successfully!")

    return redirect(url_for('main.user_home'))

@auth.route('/signup', methods=["POST"])
def signup_post():
    # Signup with email, username, password(min. 12 chars, alphanumeric, 1+ special characters)
    # Values shall be taken from the signup form; code stubs below
    email = "test@email.com"
    username = "testUser123"
    password = "testtest1234!@#"

    # Sanitise email, username, password values to remove any potential SQL injection commands.
    # If SQL injection is detected, return the user to the signup page with a generic
    # "failed to signup" error message

    # email check, ideally using 2FA ("We sent you a confirmation email" etc)
    if not re.match('.*@.*\.com', email):
        flash("Invalid email")

    if (len(password) < 12) or not re.search(r'[!@#$%^&*()_+{}|:"<>?\[\];\',./\\]', password):
        flash("Password not long enough, or missing a special character.")
    
    # Check if user already exists
    query = text("SELECT * FROM user WHERE email = :email OR username = :username")
    user = db.session.execute(query, {"email": email, "username": username}).all()
    if len(user) > 0:
        flash("User already exists")
        return redirect(url_for('auth.signup'))
    
    # Otherwise if no user already exists:
    # Hash the password with SHA256
    password = generate_password_hash(str(password), method="pbkdf2:sha256")
    new_user = User(email = email, name = name, password = password, role = "regularUser") # Admins can add themselves to the db manually
    db.session.add(new_user)
    db.session.commit()

    flash("Signup successful, please log in with your new account")

    return redirect(url_for('main.index'))


# ---------------------------------------------------------------------------------------------------
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# ---------------------------------------------------------------------------------------------------
@auth.route('/admin')
@login_required
def admin():
    #TODO: Show admin page if the user's role is 'admin', else
    # redirect them to the main page
    return