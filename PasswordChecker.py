import string
import random
import re
from fpdf import FPDF

password_list = []


def password_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars)for _ in range(size))


for x in range(1000000):
    print(f'PASSWORD LIST LENGHT IS {len(password_list)}')
    password = password_generator()

    if re.fullmatch(r"^.*(?=.*?[0-9])(?=.*?[8])(?=.*?[7]).{4,}.*$", password):
        if password[0] == str(1):
            pass
        elif password[0] == str(2):
            pass
        elif password[1] == str(1):
            pass
        elif password[1] == str(2):
            pass
        else:
            if password not in password_list:
                password_list.append(password)
                print(password)
            else:
                pass

with open('readme.txt', 'w',) as f:
    f.write('    '.join(password_list))
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=15)
text_file = open('readme.txt', 'r')
for x in text_file:
    pdf.multi_cell(0, 8, txt=x)
pdf.set_font('helvetica', size=30)
pdf.ln(6)
pdf.cell(0, 8, 'GOOD LUCK MARINA! :D:D:D', 0, 0, 'C')
pdf.output('password.pdf')
