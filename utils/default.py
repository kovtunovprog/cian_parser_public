import os
import time

from data.config import TIME_WAIT_PARSING_ITERATION
from parser.parsing_iteration import parsing_iteration
from utils.send_email import send_mail


def get_emails_from_file():
    """
    Check emails file
    :return: email list
    """

    emails = []
    with open('../emails.txt', 'r') as emails_file:
        for email in emails_file:
            emails.append(email)
    return emails or None


def parsing_process():
    """
    Process parsing and send messages to emails
    :return:
    """
    connect_to_vpn = 'windscribe connect'
    disconnect_vpn = 'windscribe disconnect'
    while True:
        try:
            os.system(connect_to_vpn)
            main_info_list = parsing_iteration()
            message = ''
            for info_list in main_info_list:
                for info_string in info_list:
                    message += info_string + '\n'
            print(message)
            if message:
                send_mail(message)
            os.system(disconnect_vpn)
        except:
            pass
        time.sleep(TIME_WAIT_PARSING_ITERATION)

