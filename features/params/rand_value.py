import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

RAND_NAME = generate_random_string(10)
RAND_EMAIL = generate_random_string(5)+'@test.ru'