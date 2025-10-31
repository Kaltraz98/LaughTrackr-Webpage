from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .Userforms import LoginForm, RegisterForm
from .models import User
from . import db

# Blueprint configuration
authbp = Blueprint('auth', __name__, url_prefix='/auth')

# Login route
@authbp.route('/login', methods=['GET', 'POST'])
def logged_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(emailid=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('You are now logged in!', 'success')
            return redirect(url_for('events.carousel'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('LoginForm.html', form=form, heading='Login')

# Register route
@authbp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(emailid=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please log in or use a different email.', 'warning')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            name=form.name.data,
            emailid=form.email.data,
            password_hash=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.logged_in'))

    return render_template('RegisterForm.html', form=form, heading='Register')

# Logout route
@authbp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))