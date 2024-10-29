# onboardapp.py
from flask import Flask, render_template
from model.onboardmodel import db  # Import db from onboardmodel.py

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localbarter.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables

    return app

app = create_app()

@app.route('/onboard')
def home():
    return "Welcome to LocalBarter!"

@app.route('/about')
def about():
    return render_template('onboard.html')

@app.route('/contact')
def contact():
    return "Contact Us Page"

@app.route('/signup')
def signup():
    return "Sign-up Page"

@app.route('/chat')
def chat():
    return "Chat Page"

if __name__ == '__main__':
    app.run(debug=True)


