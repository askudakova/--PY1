import string
from random import choice, sample

chars = string.ascii_letters + string.digits


# Вариант 1 с использованием цикла и random.choice

def get_random_password() -> str:
    password = ''
    for i in range(8):
        password += choice(chars)
    return password


print(get_random_password())


# Вариант 2 с использованием random.sample

def get_random_password2() -> str:
    return ''.join(sample(chars, 8))


print(get_random_password2())
