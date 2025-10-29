from flask import Blueprint, render_template, request, redirect, url_for, flash
from .Userforms import LoginForm, RegisterForm

# Create blueprint
authbp = Blueprint('auth', __name__, url_prefix='/auth')

# Login route
@authbp.route('/login', methods=['GET', 'POST'])
def logged_in():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        print('Successfully logged in')
        flash('You logged in successfully')
        return redirect(url_for('auth.login'))
    return render_template('LoginForm.html', form=loginForm, heading='Login')

# Register route
@authbp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Successfully registered')
        return redirect(url_for('auth.login'))
    return render_template('RegisterForm.html', form=form, heading='Register')