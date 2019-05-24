import os
import random
import string

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def save_content(path, header_name, new):
    name = path + header_name + randomString(5) + '_' + randomString(10)
    with open(name, 'w', encoding='utf8') as file:
        file.write(new)
