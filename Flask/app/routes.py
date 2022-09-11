# applikation/app/routes.py
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import LoginForm, ResetPasswordRequestForm

# Route for Startseite
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Herzlich willkommen'}
    return render_template('index.html', title='Startseite', user=user)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login durchgeführt für user {}, anmeldung_merken={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='anmelden', form=form)


# route for handling passwort reset request
@app.route('/resetpwd', methods=['GET', 'POST'])
def resetpwd():
    form = ResetPasswordRequestForm()
    return render_template('resetpwd.html',
                           title='Passwort zurücksetzen', form=form)

# route for Registration Platfrom
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

# route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')