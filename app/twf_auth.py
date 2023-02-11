import random
import string
import smtplib
import time
from flask import current_app
from threading import Timer


def verification_process():
    is_gen = False

    def verify():
        nonlocal is_gen
        code = ""
        if not is_gen:
            def generate_random_code():
                nonlocal is_gen
                """generate random code to send to the user for the verification purpose"""
                nonlocal code
                for _ in range(10):
                    random_num_sel = random.randint(1, 6)
                    if random_num_sel % 2 == 0:
                        random_val = random.choice(string.digits)
                    else:
                        random_val = random.choice(string.ascii_uppercase)
                    code += random_val

                # start a timer here
                timer = Timer(10, verify)
                timer.start()
                is_gen = True
                print('timer_executed')
                current_app.config['CODE'] = code
                return code
            return generate_random_code()
        current_app.config['CODE'] = code
        print('it is expired')
        return

    return verify()


def send_code(email):
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=current_app.config['USERNAME'],
                   password=current_app.config['PASSWORD'])
        conn.sendmail(from_addr=current_app.config["USERNAME"],
                      to_addrs=email,
                      msg=verification_process())
