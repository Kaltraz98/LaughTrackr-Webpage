# Creating and registering views in blueprints too group related views into files
# Create Blueprint
from flask import Blueprint, render_template, request, session
mainbp = Blueprint('main', __name__)

# Define Route and register blueprint
@mainbp.route('/')
def index():
    str = '<h1>Hello World</h1>'
    return str

#define login
@mainbp.route('/login', methods = ['GET', 'POST'])
def login():
    email = request.values.get("email")
    passwd = request.values.get("pwd")
    print (f"Email: {email}\nPassword: {passwd}")
    return render_template('IndexPage.html')

#define logout
@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User logged out'

