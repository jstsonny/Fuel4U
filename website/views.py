from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User, Quote  # Import the User model
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html",user = current_user)

@views.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        full_name = request.form.get('fullName')
        address_1 = request.form.get('address1')
        address_2 = request.form.get('address2')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zipcode')

        if len(full_name) < 3:
            flash('Invalid name', category='error')
        elif len(address_1) < 6:
            flash('Invalid address', category='error')
        elif len(city) < 1:
            flash('Invalid city', category='error')
        elif len(zip_code) != 5:
            if len(zip_code) !=10:
                flash('Invalid zip', category='error') 
        else:
            current_user.fullName = full_name
            current_user.address1 = address_1
            current_user.address2 = address_2
            current_user.city = city
            current_user.state = state
            current_user.zipcode = zip_code
            db.session.commit()
            flash('Account Updated!', category='success')
            return redirect(url_for('views.getquote'))
    
    return render_template("profile.html", user=current_user)

@views.route('/get_quote', methods=['GET', 'POST'])
def getquote():
    if request.method == "POST":
        gallons = int(request.form.get('gallonsRequested'))
        date = request.form.get('deliveryDate')
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        state = current_user.state
        address = current_user.address1
        quote = Quote(gallons_requested=gallons, delivery_date=date_obj, user=current_user, state=state, address=address)

        db.session.add(quote)
        db.session.commit()

        return redirect(url_for('views.getquote'))

    latest_quote = Quote.query.filter_by(user_id=current_user.id).order_by(Quote.id.desc()).first()

    return render_template("getquote.html", user=current_user, quote=latest_quote)


@views.route('/quote_history')
def quotehistory():
    return render_template("quotehistory.html", user=current_user)