import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Myself'
email['to'] = 'myself@example.com'
email['subject'] = 'Something Important Inside'

email.set_content(html.substitute({'name': 'Mark'}), html)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()         # encryption mechanism to connect to server
    smtp.login('myemail@gmail.com', 'mypassword')
    smtp.send_message(email)
    print('All done!')
