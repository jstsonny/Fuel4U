from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean = True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #when adding database, we are going to add conditions to already existing user

        if password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            flash('Account created!', category='success')
            #return redirect(url_for('views.profile'))
        
    return render_template("signup.html")

