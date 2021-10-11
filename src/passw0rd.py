import random

numbers = "0123456789"
low = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()-_=+~[]/;[]|}{>?<"
characters = numbers + low + upper + symbols


def generate(length=64, characters=characters):
    pwd = []
    for count in range(length):
        choice = random.choice(characters)
        pwd.append(choice)
        del choice
    return ''.join(str(item) for item in pwd)

def is_secure(pwd: str):
    length = len(pwd)
    
    if length <= 10:
        return "TOTALLY UNSAFE"
    elif length > 10 and length < 20:
        return "UNSAFE"
    elif length > 20 and length < 30:
        return "NOT ENOUGH SAFE"
    elif length > 30 and length < 40:
        return "GOOD ENOUGH"
    elif length > 40 and length < 50:
        return "VERY GOOD"
    elif length > 50 and length < 60:
        return "EXCELLENT"
    elif length > 60 and length < 64:
        return "PERFECT"
