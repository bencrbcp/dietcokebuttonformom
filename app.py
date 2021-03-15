from flask import Flask, render_template, request
import time
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    time.sleep(1.5)
    if request.method == 'POST':
        # email_alert("New Diet Coke Alert", "Hello World", "dafije8395@naymeo.com")
        # email_alert("asjlfhjldshjlfsdjlfds", "ptrwreteridfpso", "9548127501@mms.att.net")
        return render_template('success.html')






def email_alert(subject, body, to):
    user = "dietcokebuttonformom@gmail.com"
    password = "xrawcgapakabxrwo"

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    app.debug = True
    app.run()
