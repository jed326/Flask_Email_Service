from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)

with open("credentials.txt", "r") as file:
    username, password = file.read().split()

#BUG: SSL_WRONG_VERSION
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    # MAIL_USE_TLS = True,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = username,
    MAIL_PASSWORD = password,
))

mail = Mail(app)

@app.route('/')
def index():
    return "/send to send an email"

#TODO: Look up gmail message specs
@app.route('/send')
def email():
    msg = Message("Hello",
                  sender=("Jay Deng", "me@example.com"),
                  recipients=["jayd0104@gmail.com"])
    mail.send(msg)
    return

"""
{
    "name" : "Name",
    "email" : "email@address.com",
    "subject" : "Subject",
    "message" : "Message body"
}
"""


@app.route('/post', methods=['POST'])
def json_example():
    data = request.get_json()
    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']

    return "%s, %s, %s, %s" % (name, email, subject, message)
