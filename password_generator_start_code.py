import string
import random
all_alphabets = list(string.ascii_letters)
#print(f"these are all english alphabets {all_alphabets}")

all_digits = list(string.digits)
#print(f"these are all digits {all_digits}")

all_symbol = list(string.punctuation)
#print(f"these are all symbols {all_symbol}")

number_of_letters =int(input("How many letters would do you like in your password?"))
#print(f"you have chosen {number_of_letters} letters")
number_of_symbols = input("How many symbols would you like in your password?")
number_of_digits = input("how many digits would you like in your password?")

# set accumulator for password character list
# Randomly select the characters 

password_character_list  = []
for number in range(number_of_letters):
    random_letter = random.choice(all_alphabets)
    password_character_list.append(random_letter)

# Set accumulator for password digit list
# Randomly select the number 
password_digit_list = []
for digit in range(int(number_of_digits)):
    random_digit = random.choice(all_digits)
    password_digit_list.append(random_digit)

# Set accumulator for password digit list
# Randomly select the number 
password_symbol_list = []
for symbol in range(int(number_of_symbols)):
    random_symbol = random.choice(all_symbol)
    password_symbol_list.append(random_symbol)

# Getting final password by adding digits, letter, and symbol sublist
final_password_list = password_character_list + password_digit_list + password_symbol_list
#shuffling the final password 
random.shuffle(final_password_list)

#converting the final password Array to string
full_password=""
#traversing the list
for character in final_password_list:
    full_password += character
print(full_password)
