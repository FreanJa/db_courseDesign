from flask import Flask
import sql_server

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    print(sql_server.search_template())
    # return 'Hi Flask👋!'
    return sql_server.search_template()


if __name__ == '__main__':
    app.run(debug=True)
