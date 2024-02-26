import random
import string

"""
A class that generates a random passwords that is 32 characters in length and
contains 30% lowercase letters, 20% uppercase letters, 10% digits and 10% special characters.
"""


class Passwords:
    def __init__(self):
        self.l1 = list(string.ascii_lowercase)
        self.l2 = list(string.ascii_uppercase)
        self.l3 = list(string.digits)
        self.l4 = list(string.punctuation)

        self.part1 = None
        self.part2 = None

        self.result = []

    def shuffle_lists(self):
        random.shuffle(self.l1)
        random.shuffle(self.l2)
        random.shuffle(self.l3)
        random.shuffle(self.l4)

    def character_distribution(self, length: int):
        self.part1 = round(length * (30 / 100))
        self.part2 = round(length * (20 / 100))

    def character_generation(self):
        for i in range(self.part1):
            self.result.append(self.l1[i])
            self.result.append(self.l2[i])
        for i in range(self.part2):
            self.result.append(self.l3[i])
            self.result.append(self.l4[i])

    def generate_password(self):
        self.shuffle_lists()
        self.character_distribution(32)
        self.character_generation()

        random.shuffle(self.result)
        password = "".join(self.result)
        return password


# pw = Passwords()
# print(pw.generate_password())
