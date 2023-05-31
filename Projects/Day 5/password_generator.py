# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# character = ""

# for num in range(1,nr_letters + 1):
#     rd_letter=random.choice(letters)
#     character +=rd_letter

# symbol =""
# for num in range(1,nr_symbols + 1):
#     symbol +=random.choice(symbols)

# numb =""
# for num in range(1,nr_numbers + 1):
#     numb +=random.choice(numbers)

# password = character + symbol +numb
# random.shuffle(password)
# print(password  )



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

character = []
for num in range(1,nr_letters + 1):
    rd_letter=random.choice(letters)
    character +=rd_letter

for num in range(1,nr_symbols + 1):
    character +=random.choice(symbols)

for num in range(1,nr_numbers + 1):
    character +=random.choice(numbers)

random.shuffle(character)

y =""
for x in character:
    y +=x 

print(f"Your password is: {y}")

