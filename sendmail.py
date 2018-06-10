#!/usr/bin/python 
import smtplib
from email.mime.text import MIMEText

FROM = 'admin@fake.host'
TO   = ['admin@localhost']
SUBJECT = 'Test'
TEXT = 'A text sent with Python\'s smtplib'
MESSAGE = """
FROM: %s
TO: %s
SUBJECT: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

s = smtplib.SMTP('localhost', 8025)
s.sendmail(FROM, TO, MESSAGE.encode('utf-8'))
s.quit()
