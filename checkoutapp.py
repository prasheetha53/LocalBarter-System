# checkoutapp.py
from flask import Flask, render_template, jsonify, request, redirect, url_for
from model.checkoutmodel import add_to_cart, update_quantity, get_cart_items, get_contact_details, set_contact_details

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('checkout'))

@app.route('/checkout')
def checkout():
    cart_items = get_cart_items()
    contact_details = get_contact_details()
    return render_template('checkout.html', cart_items=cart_items, contact_details=contact_details)

@app.route('/update_exchange', methods=['POST'])
def update_exchange():
    data = request.json
    for item in data['items']:
        update_quantity(item['id'], item['quantity'])
    return jsonify({"message": "Exchange updated!"})

@app.route('/confirm_location', methods=['POST'])
def confirm_location():
    phone = request.form.get("phone")
    email = request.form.get("email")
    location = request.form.get("location")
    set_contact_details(phone, email, location)
    return jsonify({"message": "Location confirmed!"})

if __name__ == '__main__':
    app.run(debug=True)
