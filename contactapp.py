from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('contact.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        # Here you can handle the form submission, e.g., saving to a database or sending an email.
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")
        return "Message sent!"  # Redirect or render a response after form submission
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
