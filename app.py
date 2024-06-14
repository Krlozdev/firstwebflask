from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return 'Hello World!'

@app.route('/clase')
def clase():
    return '<h1><center>Clase de fundamentos de programacion</center></h1>'


if __name__ == '__main__':
    app.run()
