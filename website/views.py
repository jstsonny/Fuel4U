from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html",user = current_user)

@views.route('/profile', methods=['GET','POST'])
def profile():
    return render_template("profile.html")

@views.route('/get_quote')
def getquote():
    return render_template("getquote.html")

@views.route('/quote_history')
def quotehistory():
    return render_template("quotehistory.html")