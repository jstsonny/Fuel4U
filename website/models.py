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
    zipcode = db.Column(db.String(10),nullable = True)
    quotes = db.relationship('Quote', back_populates='user', lazy=True)  
    def get_id(self):
        return self.username

    
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallons_requested = db.Column(db.Float, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    suggested_price = db.Column(db.Float)
    total_amount_due = db.Column(db.Float)
    state = db.Column(db.String(2))
    address = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates="quotes")

    def __init__(self, gallons_requested, delivery_date, user, state, address):
        self.gallons_requested = gallons_requested
        self.delivery_date = delivery_date
        self.user_id = user.id
        self.user = user
        self.state = state
        self.address = address
        self.calculate_suggested_price()
        self.calculate_total_amount_due()

    def calculate_suggested_price(self):
        # Calculate the margin based on the factors
        current_price = 1.50  # Constant current price per gallon
        location_factor = 0.02 
        if self.state == 'TX':
            location_factor = 0.02 
        else: 
            location_factor = 0.04
        if len(self.user.quotes) > 0:
            rate_history_factor = 0.01
        else:
            rate_history_factor = 0.00
            
        gallons_requested_factor = 0.02 if self.gallons_requested > 1000 else 0.03
        company_profit_factor = 0.10

        margin = current_price * (location_factor - rate_history_factor + gallons_requested_factor + company_profit_factor)

        # Calculate the suggested price
        self.suggested_price = current_price + margin

    def calculate_total_amount_due(self):
        # Calculate the total amount due based on the suggested price and gallons requested
        self.total_amount_due = self.suggested_price * self.gallons_requested

