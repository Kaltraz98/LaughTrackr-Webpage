from flask import Blueprint, render_template

# name - first argument is the blueprint name 
# import name - second argument - helps identify the root url for it 
destbp = Blueprint('NewEvent', __name__, url_prefix='/New-Event')

@destbp.route('/<id>')
def show(id):
    return render_template('EventCreationPage.html')
