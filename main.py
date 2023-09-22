# TODO hacer un programa de recordatorios con correo electronico,
# pedira clave de correo al usuario y podra hacer entradas con fecha,
# que sera cuando se le enviara el correo.

import utils
from getpass import getpass

def main():
    sender = input("Your gmail: ")
    password = getpass()
    recipient = input("Send mail to: ")
    subject = input("Subject: ")
    body = input("Body: ")

    utils.send_mail(sender, password, recipient, subject, body)
    print("Message sent!")

main()
