import random
import string

letters = string.ascii_letters
car = ""

while car != "t":
    car = random.choice(letters)
    print(f"Le caractère choisi est {car}")
