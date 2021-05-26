import random
import re
from fpdf import FPDF
import time

password_list = []


def password_check():
    start = time.time()

    def password_generator():
        security_number = []
        security_string = ''
        for x in range(1):
            security_number.append(random.randrange(3, 10))
            security_number.append(random.randrange(0, 10))
            if security_number[0] == security_number[1]:
                break
            else:
                security_number.append(random.randrange(0, 10))
                if security_number[1] == security_number[2]:
                    break
                else:
                    security_number.append(random.randrange(0, 10))
                    if security_number[2] != security_number[3]:
                        security_string = ''.join(str(item)
                                                  for item in security_number)
        return security_string

    for x in range(1000000):

        password = password_generator()
        if len(password) == 4:

            if re.fullmatch(r"^.*(?=.*?[0-9])(?=.*?[8])(?=.*?[7]).*$", password):

                if password not in password_list:
                    password_list.append(password)

    end = time.time()
    print(f'It took {end-start} seconds to complete')


password_check()


print(f'PASSWORD LIST LENGHT IS {len(password_list)}')

password_list.sort()
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
pdf.cell(0, 8, 'GOOD LUCK !', 0, 0, 'C')
pdf.output('password.pdf')
print('JOB DONE, ALL GOOD!')
