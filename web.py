from flask import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)

with open("credentials.txt", "r") as file:
    username, password = file.read().split()

#TODO: Hide info on github
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = username,
    MAIL_PASSWORD = password,
))

mail = Mail(app)

#TODO: Look up gmail message specs
@app.route('/')
def email():
    msg = Message("Hello",
                  sender=("Jay Deng", "me@example.com"),
                  recipients=["jayd0104@gmail.com"])
    mail.send(msg)
    return
