

import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy version
password = ""
for _ in range(nr_letters):
    password += random.choice(letters)
for _ in range(nr_symbols):
    password += random.choice(symbols)
for _ in range(nr_numbers):
    password += random.choice(numbers)
print(password)

# Hard version - shuffled order
password_list = []
for _ in range(nr_letters):
    password_list.append(random.choice(letters))
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = "".join(password_list)
print(password)