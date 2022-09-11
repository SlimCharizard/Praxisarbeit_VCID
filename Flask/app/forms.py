# applikation/app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#Form for Login-Page
class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Erinnern')
    submit = SubmitField('Anmelden')
    
# Form for Passwort reset function
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Anfrage für Passwort-Reset')

#form for publishing contents as logged in user
class PublishForm(FlaskForm):
    TextTitel = StringField('Titel:', validators=[DataRequired()])
    TextFeld = StringField('Bitte hier Artikelberschreibung einfügen', validators=[DataRequired()])
    publish = SubmitField('publizieren')
