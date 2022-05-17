import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(subject, body):
    from_email = 'cmpe275.monitoring@gmail.com'
    to_email = 'sandesh.gupta93@gmail.com'
    temp = "@321"

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email

    part2 = MIMEText(body, "html")
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_email, temp)
        server.sendmail(
            from_email, to_email, message.as_string()
        )

