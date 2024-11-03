# Go to our email and setup 2 factor authentication
# Generate app password
# Create a function to send the mail


from email.message import EmailMessage
from key import pass_word
import ssl
import smtplib

email_sender = 'kamalesh.py@gmail.com'
email_password = pass_word

email_receiver = 'sinanoc581@evasud.com'

subject = "Hey, I am sending this email from a python program which I learnt from tomi on youtube"

body = '''
When you learn python just enjoy it, buddy!
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  
   smtp.login(email_sender, email_password)
   smtp.sendmail(email_sender, email_receiver, em.as_string())