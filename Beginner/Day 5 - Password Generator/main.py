# Project Day 5 : PyPassword Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("how many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many symbols would you like?\n"))
nr_numbers = int(input(f"how many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
generated_password = ""
list = []


#for example if we use a random choice
# rando.choice(letter) ==> get a rander character from the list

for i in range(nr_letters):
    random_val_i = random.randint(0, len(letters)-1)
    list += letters[random_val_i]
for j in range(nr_symbols):
    random_val_j = random.randint(0, len(symbols)-1)
    list += symbols[random_val_j]
for k in range(nr_numbers):
    random_val_k = random.randint(0, len(numbers) - 1)
    list += numbers[random_val_k]
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# To randomly reorder a list we can simply use random.shuffle(list)
random.shuffle(list)

for i in range(len(list)):
    generated_password+=list[i]
print(generated_password)
