import os
import smtplib
from email.mime.text import MIMEText
import urllib2

ip = urllib2.urlopen("http://169.254.169.254/latest/meta-data/public-ipv4").read()

def prompt(prompt):
    return raw_input(prompt).strip()

class MailService():

    def __init__(self):
        self.base_url = ip+"/project/view?"

    def sendMail(self, to_email, name, url):
        ms = """
        Hello, """+name+"""

        We are glad to inform you that the design that you uploaded to design match is already Available on the company's site.

        The url of the company is: """+self.base_url+url+"""


        Thank you for your contribution!

        Design Match staff!"""

        msg = MIMEText(ms)

        msg['to'] = to_email
        msg['from'] = 'cloud.designmatch@gmail.com'
        msg['subject'] = 'Your design have been processed!'

        smtp_server = 'email-smtp.us-east-1.amazonaws.com'
        smtp_username = os.environ["smtp_user"]
        smtp_password = os.environ["smtp_password"]
        smtp_port = '587'
        smtp_do_tls = True

        server = smtplib.SMTP(
            host = smtp_server,
            port = smtp_port,
            timeout = 10
        )
        server.set_debuglevel(10)
        server.starttls()
        server.ehlo()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg['from'], [to_email], msg.as_string())
        server.quit()