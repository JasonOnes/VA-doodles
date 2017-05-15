""" Checkst the website is it christmas and sends an email when it is. Stupid
but easily modified to send email when say datetime = June12 or quarterly, yearly
whenever investor chooses her timestamp for increment."""

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "christmas_alerts@pythonscraping.com"
    msg['To'] = "jasor.jones14@gmail.com" # or user's address obvs

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

bsObj = BeautifulSoup(urlopen('https://isitchristmas.com/'))
while(bsObj.find("a", {"id":"answer"}).attrs['title'] == "No"):
    print("It ain't christmas yet!")
    time.sleep(3600)
bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
sendmail("It's XMas","according to https://isitchristmas")
