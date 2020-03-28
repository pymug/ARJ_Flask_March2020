from flask import Blueprint, render_template

demo = Blueprint('demo', __name__, url_prefix='/demo')

@demo.route('/')
def index():
    return 'abcd'