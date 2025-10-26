from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__, url_prefix='/homepage')

@mainbp.route('/homepage')
def index():
    return render_template('IndexPage.html')

