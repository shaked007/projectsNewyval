import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail_newval():
    smtp_server = 'edge.idf.il'
    smtp_port = 35

    subject = 'subject'
    message = 'my message'
    from_email = 's8704173@army.idf.il'
    to_email = 's8704173@army.idf.il'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as SERVER:
        server.starttls()
        #server.login('user','pass')
        server.send_message(msg)

    print('mail sent')