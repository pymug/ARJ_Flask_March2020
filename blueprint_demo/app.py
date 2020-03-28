from flask import Flask
from views.demo import demo

app = Flask(__name__)


app.register_blueprint(demo)

@app.route('/')
def hello_world():
   return 'Hi Mauritius'


if __name__ == '__main__':
   app.run()