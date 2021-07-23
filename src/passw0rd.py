import random


class Generator:
    def __init__(self):
        # Characters
        self.numbers = "1234567890"
        self.low = "qwertyuiopasdfghjklzxcvbnm"
        self.upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.symbols = "!@#$%^&*()-_=+~[]/;[]|}{:>?<"
        self.characters = self.numbers + self.low + self.upper + self.symbols

        # Characters List
        self.pwd = []

    def generate(self, length=64):
        # Program
        for count in range(length):
            choice = random.choice(self.characters)
            self.pwd.append(choice)
            del choice

        # Turns the pwd list into a string
        pwd = ''.join(str(item) for item in self.pwd)

        return pwd
