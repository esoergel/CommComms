from time import sleep
from flask import Flask, request, Response
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!\n'


@app.route('/login/', methods=['POST'])
def login():
    return "logging in user %s" % request.form['username']


@app.route('/msg/', methods=['POST'])
def send_message():
    return 'received message "{message}", sending to {recipient}'.format(
        message=request.form['message'],
        recipient=request.form['recipient'],
    )


@app.route('/poll/', methods=['GET'])
def poll_for_new_messages():
    def generate():
        for i in xrange(100):
            sleep(.5)
            yield '{"status": null}\n'
    return Response(generate(), content_type="application/json")


if __name__ == '__main__':
    app.run()
