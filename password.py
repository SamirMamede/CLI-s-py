import random
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
SIMBOLS = '@%#_-+=,.'

def generate_password(letters=8, numbers=4, simbols=2):
    generated = ""
    for i in range(letters):
        generated += random.choice(LETTERS)
    for i in range(numbers):
        generated += random.choice(NUMBERS)
    for i in range(simbols):
        generated += random.choice(SIMBOLS)
    generated = list(generated)
    random.shuffle(generated)
    return ''.join(generated)

if __name__ == '__main__':
    print(generate_password())