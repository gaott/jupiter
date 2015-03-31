# -*- coding: utf-8 -*-  
'''
Created on 2013年7月1日

@author: gaott
'''
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.utils import COMMASPACE
import smtplib

def sendEmail(body):
    strFrom = 'example@gmail.com'
    strTo = ['abc@xxx.com','efg@xxx.com']
    subject = 'Warning Message'

    server = 'smtp.gmail.com'
    port = 25
    user = "example@gmail.com"
    passwd = "******"

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = strFrom
    msgRoot['To'] = COMMASPACE.join(strTo)
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    
    msgText = MIMEText(body, 'plain', 'utf-8')
    msgAlternative.attach(msgText)

    smtp = smtplib.SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user, passwd)
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()
    return

if __name__ == '__main__':
    sendEmail("hello")
