import string
import random
import re
import PyPDF2


def password_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars)for _ in range(size))


if re.fullmatch(r"^.*(?=.*?[0-9])(?=.*?[8])(?=.*?[7]).{4,}.*$", password_generator()):
    print('Match found!')
else:
    pass
