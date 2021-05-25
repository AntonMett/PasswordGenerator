import random
import re
from fpdf import FPDF

password_list = []


def password_generator():
    security_number = []
    password_string = ''
    security_number.append(random.randrange(3, 10))
    security_number.append(random.randrange(0, 10))
    if security_number[0] != security_number[1]:
        security_number.append(random.randrange(0, 10))
        if security_number[1] != security_number[2]:
            security_number.append(random.randrange(0, 10))
            if security_number[2] == security_number[3]:
                security_number = []
    if len(security_number) == 4:
        password_string = (
            f'{security_number[0]}{security_number[1]}{security_number[2]}{security_number[3]}')
    return(password_string)


for x in range(1000000):

    password = password_generator()

    if re.fullmatch(r"^.*(?=.*?[0-9])(?=.*?[8])(?=.*?[7]).*$", password):

        if password not in password_list:
            password_list.append(password)
            print(len(password_list))

print(f'PASSWORD LIST LENGHT IS {len(password_list)}')

password_list.sort()
print(password_list)
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
pdf.cell(0, 8, 'GOOD LUCK MOM! :D:D:D', 0, 0, 'C')
pdf.output('password.pdf')
