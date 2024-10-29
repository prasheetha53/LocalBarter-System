from flask import Flask, render_template, jsonify
from model.product_detailmodel import add_like, add_exchange, add_to_cart

app = Flask(__name__)

@app.route('/')
def product_detail():
    return render_template('product_detail.html')

@app.route('/like', methods=['POST'])
def like():
    add_like("Hario HY-92 Gamepad")
    return jsonify({"message": "Liked and added to wishlist!"})

@app.route('/exchange', methods=['POST'])
def exchange():
    add_exchange("Hario HY-92 Gamepad")
    return jsonify({"message": "Exchange initiated!"})

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart_route():
    add_to_cart("Hario HY-92 Gamepad")
    return jsonify({"message": "Added to cart!"})

if __name__ == '__main__':
    app.run(debug=True)
