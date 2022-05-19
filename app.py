from flask import Flask

app = Flask(__name__)


@app.route('/testFlask')
def hello_world():  # put application's code here
    return 'Hi Flask👋!'


if __name__ == '__main__':
    app.run()
