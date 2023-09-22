import smtplib
from email.mime.text import MIMEText

def send_mail(sender, password, recipient, subject, body):
    """
    The function `send_mail` sends an email using the SMTP protocol with Gmail as the email service
    provider.
    
    :param sender: The email address of the sender
    :param password: The password parameter is the password for the sender's email account. It is used
    to authenticate the sender when logging in to the SMTP server and sending the email
    :param recipient: The recipient parameter is the email address of the person or entity you want to
    send the email to
    :param subject: The subject of the email. It is a string that represents the subject line of the
    email
    :param body: The "body" parameter is the content or message of the email that you want to send. It
    can be a string containing any text or HTML content that you want to include in the email
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())
