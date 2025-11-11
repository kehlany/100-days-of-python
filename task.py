import random
letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
total = []
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
for nr_letters in range(1, nr_letters + 1):
    total.append(random.choice(letters))
nr_symbols = int(input(f"How many symbols would you like?\n"))
for nr_symbols in range(1, nr_symbols + 1):
    total.append(random.choice(symbols))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for nr_numbers in range(1, nr_numbers + 1):
    total.append(random.choice(numbers))
print(total)
random.shuffle(total)
print(total)
password = ''
for word in total:
    password += word
print(password)
