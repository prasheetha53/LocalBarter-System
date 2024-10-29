# onboardmodel.py
'''from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize the SQLAlchemy instance

# User Model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    items = db.relationship('Item', backref='user', lazy=True)

# Item Model
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# BarterTransaction Model
class BarterTransaction(db.Model):
    __tablename__ = 'barter_transaction'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    matched_item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'Pending', 'Completed', etc.

    # Relationships to fetch item details
    item = db.relationship('Item', foreign_keys=[item_id], backref='initiated_transactions')
    matched_item = db.relationship('Item', foreign_keys=[matched_item_id], backref='matched_transactions')
'''


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()  # Initialize the SQLAlchemy instance

# User Model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    items = db.relationship('Item', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Item Model
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    transactions = db.relationship('BarterTransaction', backref='item', lazy=True)

    def __repr__(self):
        return f'<Item {self.name}>'

# BarterTransaction Model
class BarterTransaction(db.Model):
    __tablename__ = 'barter_transaction'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    matched_item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'Pending', 'Completed', etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships to fetch item details
    item = db.relationship('Item', foreign_keys=[item_id], backref='initiated_transactions')
    matched_item = db.relationship('Item', foreign_keys=[matched_item_id], backref='matched_transactions')

    def __repr__(self):
        return f'<BarterTransaction {self.id}, Status: {self.status}>'
