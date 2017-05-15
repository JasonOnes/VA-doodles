""" Need to set up as an STMP client locally, if not change localhost to remote
servers address."""

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("this is a test, this is only a test")

msg['Subject'] = "An Email alert"
msg['From'] = 'jasonr.jones14@gmail.com'
msg['To'] = 'jasonr.jones14@gmail.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
