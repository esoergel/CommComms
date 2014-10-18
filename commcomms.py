from time import sleep
from flask import Flask, request, Response


app = Flask(__name__)
app.debug = True


MESSAGE_QUEUE = {}


@app.route('/')
def hello_world():
    return 'Hello World!\n'


@app.route('/login/', methods=['POST'])
def login():
    # TODO return an authentication token
    return "logging in user %s" % request.form['username']


@app.route('/msg/', methods=['POST'])
def send_message():
    message = request.form['message']
    recipient = request.form['recipient']
    print message, recipient

    if not recipient in MESSAGE_QUEUE:
        MESSAGE_QUEUE[recipient] = []
    MESSAGE_QUEUE[recipient].append(message)

    from pprint import pprint
    pprint(MESSAGE_QUEUE)
    return 'received message "{message}", sending to {recipient}'.format(
        message=message,
        recipient=recipient,
    )


@app.route('/poll/', methods=['GET'])
def poll_for_new_messages():
    user = request.authorization['username']
    print user
    def generate():
        while True:
            sleep(.5)
            if MESSAGE_QUEUE.get(user, None):
                message = MESSAGE_QUEUE[user].pop(0)
                print "sending message to {}: {}".format(user, message)
                yield "{}\n".format(message)
    return Response(generate(), content_type="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True)
