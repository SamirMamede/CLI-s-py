import random
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
SIMBOLS = '@%#_-+=,.'

def generate_password(letters=8, numbers=4, simbols=2):
    generated = ""
    generated += random_chars(letters, LETTERS)
    generated += random_chars(numbers, NUMBERS)
    generated += random_chars(simbols, SIMBOLS)
    return shuffle_strings(generated)

def random_chars(lenght, chars):
    generated = ""
    for i in range(lenght):
        generated += random.choice(chars)
    return generated

def shuffle_strings(text):
    text = list(text)
    random.shuffle(text)
    return ''.join(text)

if __name__ == '__main__':
    print(generate_password())