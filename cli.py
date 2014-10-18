import requests
import threading
import time


def login(username):
    print requests.post('http://127.0.0.1:5000/login/', data={'username': username}).text


def logout(username):
    print "user %s is logged out" % username


def send(message):
    data = {'message': "Hi there!",
            'recipient': "Nick"}
    print requests.post('http://127.0.0.1:5000/msg/',
                        data=data).text


class NewMessagePoller(threading.Thread):
    def run(self):
        print "Polling server..."
        response = requests.get('http://127.0.0.1:5000/poll/', stream=True)
        for line in response.iter_lines(chunk_size=1):
            print "Nick:", line


def receive(message):
    print "received message:\n%s" % message


if __name__ == '__main__':
    login('esoergel')
    poller = NewMessagePoller()
    poller.start()
    logout('esoergel')
