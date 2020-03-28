from flask import Blueprint, render_template

demo2 = Blueprint('demo2', __name__, url_prefix='/demo2')

@demo2.route('/') #
def index():
    return render_template('demo2/index.html')

@demo2.route('/greet') #
def greet():
    return 'hi!'