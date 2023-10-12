from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

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
            flash('Account Updated!', category='success')
            return redirect(url_for('views.getquote'))
    
    return render_template("profile.html")

@views.route('/get_quote')
def getquote():
    return render_template("getquote.html")

@views.route('/quote_history')
def quotehistory():
    return render_template("quotehistory.html")