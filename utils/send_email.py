import logging

import smtplib
from smtplib import SMTP

from data.config import smtp_server, smtp_port, sender_email, email_password
from loader import emails


message_format = """\
Subject: Оповещение

{}
"""


def send_mail(message: str):
    """

    :param message:
    :return:
    """
    server: SMTP = smtplib.SMTP(smtp_server, smtp_port)
    # emails = ['maxim.kliakhin@gmail.com', 'mailsenderbot889@gmail.com', 'kovtunov.prog@gmail.com']
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, email_password)
    # print(message_format.format(message))
    for email in emails:
        server.sendmail(sender_email, email, message_format.format(message).encode('utf-8').strip())
    server.quit()
    print('Already send')