# wishlistapp.py

from flask import Flask, render_template, request, redirect, url_for, jsonify
from wishlistmodel import WishlistModel

app = Flask(__name__)
wishlist_model = WishlistModel()

@app.route('/')
def wishlist_page():
    # Retrieve wishlist items from the database
    wishlist_items = wishlist_model.get_wishlist()
    return render_template('wishlist.html', items=wishlist_items)

@app.route('/add', methods=['POST'])
def add_to_wishlist():
    item_name = request.form['item_name']
    image_url = request.form['image_url']
    exchange_value = int(request.form['exchange_value'])

    # Add item to wishlist
    wishlist_model.add_to_wishlist(item_name, image_url, exchange_value)

    return redirect(url_for('wishlist_page'))

@app.route('/remove/<int:item_id>', methods=['POST'])
def remove_from_wishlist(item_id):
    # Remove item from wishlist
    wishlist_model.remove_from_wishlist(item_id)
    return redirect(url_for('wishlist_page'))

@app.route('/api/wishlist', methods=['GET'])
def get_wishlist_api():
    # API endpoint to retrieve wishlist items
    wishlist_items = wishlist_model.get_wishlist()
    return jsonify(wishlist_items)

if __name__ == '__main__':
    app.run(debug=True)
