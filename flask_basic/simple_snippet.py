from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/add/<int:num1>/<int:num2>')
def hello_world(num1, num2):
    total = num1 + num2
    return str(total)

@app.route('/')
def index():
    y = 1 + 2
    return render_template('index.html', 
        addition=str(y))


if __name__ == '__main__':
   app.run(debug=True)