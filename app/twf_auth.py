import random
import string
import smtplib
from flask import current_app


def generate_random_code():
    """generate random code to send to the user for the verification purpose"""
    code = ''
    for _ in range(10):
        random_num_sel = random.randint(1, 6)
        if random_num_sel % 2 == 0:
            random_val = random.choice(string.digits)
        else:
            random_val = random.choice(string.ascii_uppercase)
        code += random_val
    return code

# saves the code to check for the verification


def send_code(email):
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=current_app.config['USERNAME'],
                   password=current_app.config['PASSWORD'])
        conn.sendmail(from_addr=current_app.config["USERNAME"],
                      to_addrs=email,
                      msg=generate_random_code())
