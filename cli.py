import requests



def login(username):
    print "user %s is logged in" % username
    print requests.post('http://127.0.0.1:5000/login/', data={'username': username}).text

def logout(username):
    print "user %s is logged out" % username


def send(message):
    print "sending message:\n%s" % message


def receive(message):
    print "received message:\n%s" % message


if __name__ == '__main__':
    login('esoergel')
    send('first message')
    receive('receiving message')
    logout('esoergel')
