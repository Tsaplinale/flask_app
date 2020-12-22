from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Решено! ВМ взяли новую, добавили authorized_keys, устновили докер в ВМ'
'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
