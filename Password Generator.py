letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
print("Welcome to the Password Generator")
password=[]
password_letters=int(input("How many letters would you like in your password? "))
password_numbers=int(input("How many numbers would you like in your password? "))
password_symbols=int(input("How many symbols would you like in your password? "))

for letter in range(0,password_letters):
    password += random.choice(letters)
for number in range(0,password_numbers):
    password += random.choice(numbers)
for symbol in range(0,password_symbols):
    password += random.choice(symbols)

random.shuffle(password)
password = "".join(password)
print(f"Your Password is {password}")
