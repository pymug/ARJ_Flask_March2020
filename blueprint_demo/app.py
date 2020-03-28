from flask import Flask
from views.demo import demo
from views.demo2 import demo2

app = Flask(__name__)


app.register_blueprint(demo)
app.register_blueprint(demo2)

@app.route('/')
def hello_world():
   return 'Hi Mauritius'


if __name__ == '__main__':
   app.run(debug=True)