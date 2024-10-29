import sys
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from model.signupmodel import db, User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localbarter.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email address already exists')
            return redirect(url_for('signup'))

        # Hash the password and save the user
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Redirecting to home page.')
            return redirect(url_for('home'))  # Redirecting to home page
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again.')
            return redirect(url_for('signup'))
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Login failed. Check your email and/or password')
            return redirect(url_for('login'))

        flash('Logged in successfully!')
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/')
def home():
    return render_template('index.html')  # Ensure you render the home page

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
