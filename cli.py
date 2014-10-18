import requests
import threading
import time

SERVER = "http://127.0.0.1:5000"

def login():
    username = raw_input("What is your username?")
    return username, "guest"
    # print requests.post(SERVER + '/login/', data={'username': username}).text


def logout(username):
    print "user %s is logged out" % username


def send(raw, auth):
    recipient, message= raw.split(':')
    data = {'message': message,
            'recipient': recipient}
    requests.post(SERVER+'/msg/',
                        data=data, auth=auth).text


class NewMessagePoller(threading.Thread):
    def __init__(self, auth, *args, **kwargs):
        self.auth = auth
        super(NewMessagePoller, self).__init__(*args, **kwargs)

    def run(self):
        response = requests.get(SERVER+'/poll/',
                                stream=True, auth=self.auth)
        for line in response.iter_lines(chunk_size=1):
            print "New message!:", line


def prompt(auth):
    while True:
        message = raw_input()
        send(message, auth)


if __name__ == '__main__':
    auth = login()
    poller = NewMessagePoller(auth)
    poller.start()
    prompt(auth)
    logout('esoergel', auth)
