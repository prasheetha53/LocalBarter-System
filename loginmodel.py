from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Store hashed password in production

    def __repr__(self):
        return f'<User {self.email}>'
