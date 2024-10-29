from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('onboarding.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/swipe')
def swipe():
    return render_template('swipe.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
