from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150),unique=True)  # Define username as the primary key
    password = db.Column(db.String(150))
    fullName = db.Column(db.String(150),nullable = True)
    address1 = db.Column(db.String(150),nullable = True)
    address2 = db.Column(db.String(150),nullable = True)
    city = db.Column(db.String(150),nullable = True)
    state = db.Column(db.String(2),nullable = True)
    zipcode = db.Column(db.Integer,nullable = True)
    qoutes = db.relationship('Quote', backref='user', lazy=True)  # Assuming Quote is the correct model name
    
    def get_id(self):
        return self.username

    
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallons_requested = db.Column(db.Float, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    suggested_price = db.Column(db.Float)
    total_amount_due = db.Column(db.Float)
    user_id = db.Column(db.String(150), db.ForeignKey('user.username'), nullable=False)

    # Define a constructor to initialize fields
    def __init__(self, gallons_requested, delivery_date, user_id):
        self.gallons_requested = gallons_requested
        self.delivery_date = delivery_date
        self.user_id = user_id

    # Add methods for calculating suggested_price and total_amount_due based on your business logic
    def calculate_suggested_price(self):
        # Add your logic here to calculate the suggested price
        pass

    def calculate_total_amount_due(self):
        # Add your logic here to calculate the total amount due
        pass
