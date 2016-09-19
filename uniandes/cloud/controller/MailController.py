import os
import smtplib
from email.mime.text import MIMEText

def prompt(prompt):
    return raw_input(prompt).strip()

class MailController():

    def sendMail(self, to_email, name):
        ms = """
        Hello, """+name+"""

        Your video is already Available on the company's site.
        Thank you for your participation!"""

        msg = MIMEText(ms)

        msg['to'] = to_email
        msg['from'] = 'raulguti90@gmail.com'
        msg['subject'] = 'Your video have been processed'

        username = "raulguti90@gmail.com"
        password = "xxxxxxxxx"

        server = smtplib.SMTP('smtp.gmail.com','587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(msg['from'], msg['to'], msg.as_string())
        server.close()


