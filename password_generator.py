import random
from readline import set_completion_display_matches_hook

from soupsieve import select
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
lent= nr_letters + nr_symbols + nr_numbers
# for some in rang
password=[]
for char in range(1,nr_letters + 1):
    password.append(random.choice(letters))
for num in range(1, nr_symbols + 1):
    password.append(random.choice(numbers))
for sym in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(password)
truepass=""
for x in password:
    truepass += x
print(truepass)