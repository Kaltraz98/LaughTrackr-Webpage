from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from .models import User  # Make sure this import matches your structure

authbp = Blueprint('auth', __name__, url_prefix='/auth')

@authbp.route('/login', methods=['GET', 'POST'])
def logged_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pwd')
        user = User.query.filter_by(emailid=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')

@authbp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))