import string
import random
import re
from fpdf import FPDF

password_list = []


def password_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars)for _ in range(size))


for x in range(len(password_list) + 10000):
    print(f'PASSWORD LIST LENGHT IS {len(password_list)}')
    password = password_generator()
    print(password)
    if re.fullmatch(r"^.*(?=.*?[0-9])(?=.*?[8])(?=.*?[7]).{4,}.*$", password):
        if password[0] == str(1):
            pass
        if password[0] == str(2):
            pass
        elif password[1] == str(1):
            pass
        elif password[1] == str(2):
            pass
        else:
            if password not in password_list:
                password_list.append(password)
                print(password_list)
            else:
                pass

print(f'SKOLKO PAROLEJ {len(password_list)}')

with open('readme.txt', 'w',) as f:
    f.write('    '.join(password_list))
