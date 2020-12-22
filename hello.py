from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Получилось все же, круть!!'
'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
