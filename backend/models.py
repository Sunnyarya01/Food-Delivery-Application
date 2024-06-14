# Prepare model
from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    address = db.relationship('Address', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'role': self.role,
            'address': [address.json() for address in self.address]
        }
    
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line1 = db.Column(db.String(120), nullable=False)
    line2 = db.Column(db.String(120), nullable=True)
    pincode = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Address %r>' % self.username
    
    def json(self):
        return {
            'id': self.id,
            'line1': self.line1,
            'line2': self.line2,
            'pincode': self.pincode,
            'city': self.city,
            'state': self.state
        }