import random


class Password:
    # Characters
    numbers = "0123456789"
    low = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()-_=+~[]/;[]|}{:>?<"
    characters = numbers + low + upper + symbols

    @classmethod
    def generator(cls, length=64, duplicate_char=True, characters=characters):
        pwd = []
        for count in range(length):
            choice = random.choice(characters)
            choice = Password.duplicate(pwd, choice) if duplicate_char is False else choice
            pwd.append(choice)
            del choice

        # Turns the pwd list into a string
        pwd = ''.join(str(item) for item in pwd)

        return pwd

    @classmethod
    def duplicate(cls, array: list, char: str, characters=characters):
        for i in array:
            if i == char:
                char = random.choice(characters)
                Password.duplicate(array, char)
        return char
