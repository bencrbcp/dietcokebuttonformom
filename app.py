from flask import Flask, render_template, request
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    time.sleep(1.5)

    now = datetime.now()
    t = now.strftime("%I:%M %p")
    date = now.strftime("%D")

    if request.method == 'POST':
        # EDIT ME: To send you email alerts
        email_alert("Diet Coke Alert~", "<Person name> asked for a new Diet Coke at " + t + " on " + date + ".", "email@example.com")
        # EDIT ME: To send text message alerts
        email_alert("Diet Coke Alert~", "<Person name> asked for a new Diet Coke at " + t + " on " + date + ".", "phone_number@your_mail_carrier's_email_to_text_address") 
        return render_template('success.html')


def email_alert(subject, body, to):
    u = "dietcokebuttonformom@gmail.com"
    p = "xrawcgapakabxrwo"

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = u

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(u, p)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    app.debug = True
    app.run()
