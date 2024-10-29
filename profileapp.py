from flask import Flask, render_template, request, redirect, url_for, flash
from profilemodel import UserProfile

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# In-memory storage for demo purposes
user_profiles = {}

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        full_name = request.form['fullName']
        email = request.form['email']
        social_accounts = request.form.get('socialAccounts', '')
        address = request.form.get('address', '')
        town = request.form['town']
        phone = request.form['phone']
        zip_code = request.form['zipCode']
        
        # Create or update user profile
        profile = UserProfile(full_name, email, social_accounts, address, town, phone, zip_code)
        user_profiles[email] = profile  # Using email as a key for simplicity
        
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    # Handle GET request
    return render_template('profile.html', profile=user_profiles.get('test@example.com', None))  # Placeholder email

if __name__ == '__main__':
    app.run(debug=True)
