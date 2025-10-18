from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__)

@mainbp.route('/laughtrackr/templates')
def index():
    return render_template('IndexPage.html')