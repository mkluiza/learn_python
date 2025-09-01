# Password Genrator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")

letter_len = int(input("How many letters would you like in your password?\n"))
symbols_len = int(input(f"How many symbols would you like?\n"))
number_len = int(input(f"How many numbers would you like?\n"))


# Loop for letter_len + random choice

choice_letters = [random.choice(letters)for let in range(letter_len + 1)]
choice_numbers = [random.choice(numbers)for num in range(number_len + 1)]
choice_symbols = [random.choice(symbols)for sym in range(symbols_len + 1)]
# or range(0, letter_len)


# Combine everything
password_list = choice_letters + choice_numbers + choice_symbols

# Shuffle so it's not predictable
random.shuffle(password_list)

# Join into a final password string
password = "".join(password_list)
# "".joint : put nothing "" between the characters, just stick them together

print("Your password is:", password)
