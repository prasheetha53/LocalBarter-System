from flask import Flask, render_template, redirect, url_for
from model.settingsmodel import User, Product, Exchange

app = Flask(__name__)

# Sample data for the user, products, and exchanges
user = User(name="Rudra", email="rudra@example.com")
current_product = Product(
    name="CANON Vintage RV300D Camera",
    image_url="https://images.pexels.com/photos/51383/photo-camera-subject-photographer-51383.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
)
past_exchanges = [
    Exchange(
        user_product=Product(
            name="Pink Jacket", 
            image_url="https://images.pexels.com/photos/8413752/pexels-photo-8413752.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        ),
        exchanged_product=Product(
            name="Gray Chair", 
            image_url="https://images.pexels.com/photos/6800556/pexels-photo-6800556.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        ),
        exchange_partner="Rakesh"
    )
]

@app.route('/')
def settings():
    """Render the settings page with user data and past exchanges."""
    return render_template('settings.html', user=user, current_product=current_product, past_exchanges=past_exchanges)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear past exchanges and redirect to the settings page."""
    global past_exchanges
    past_exchanges = []  # Clear the past exchanges
    return redirect(url_for('settings'))  # Redirect to the settings page

if __name__ == '__main__':
    app.run(debug=True)
