from flask import Blueprint, render_template

# name - first argument is the blueprint name 
# import name - second argument - helps identify the root url for it 
destbp = Blueprint('Events', __name__, url_prefix='/Events')

@destbp.route('/<id>')
def show(id):
    return render_template('events.html')
