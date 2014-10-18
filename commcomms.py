from flask import Flask, request
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!\n'


@app.route('/login/', methods=['POST'])
def login():
    return "logging in user %s" % request.form['username']

if __name__ == '__main__':
    app.run()
