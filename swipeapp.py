from flask import Flask, render_template, jsonify, request
from model.swipemodel import get_next_item, add_to_wishlist

app = Flask(__name__)

@app.route('/')
def swipe():
    item = get_next_item()
    return render_template('swipe.html', item=item)

@app.route('/next-item', methods=['GET'])
def next_item():
    item = get_next_item()
    return jsonify(item)

@app.route('/add-to-wishlist', methods=['POST'])
def add_to_wishlist_route():
    item_data = request.json
    add_to_wishlist(item_data)
    return jsonify({"status": "success", "message": "Item added to wishlist"})

@app.route('/contact')
def contact():
    return "Contact Page"

@app.route('/about')
def about():
    return "About Page"

@app.route('/signup')
def signup():
    return "Sign-up Page"

@app.route('/chat')
def chat():
    return "Chat Page"

@app.route('/wishlist')
def wishlist():
    return "Wishlist Page"

@app.route('/settings')
def settings():
    return "Settings Page"

@app.route('/terms')
def terms():
    return "Terms of Service Page"

@app.route('/privacy')
def privacy():
    return "Privacy Policy Page"

if __name__ == '__main__':
    app.run(debug=True)
