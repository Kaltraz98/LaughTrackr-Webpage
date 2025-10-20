# Creating and registering views in blueprints to group related views into files
# Create Blueprint
from flask import Blueprint, render_template, request, session

# Define Route and register blueprint

# name - first argument is the blueprint name 
# import name - second argument - helps identify the root url for it 
destbp = Blueprint('login', __name__, url_prefix='/login')

@destbp.route('/<id>')
def show(id):
    return render_template('login.html')

#define login
@destbp.route('/login', methods = ['GET', 'POST'])
def login():
    email = request.values.get("email")
    passwd = request.values.get("pwd")
    print (f"Email: {email}\nPassword: {passwd}")
    return render_template('IndexPage.html')

#define logout
@destbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User logged out'

