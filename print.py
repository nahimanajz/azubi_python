name = raw_input('What is your name?') #read input from user
print('Hello')
print(name)
# use double print to set new line
print("hello")
print("world")

# using \n to insert newline
print(" set new line \n here")

#concatenting strings
first_name = "Janvier"
second_name = "Na"
full_name = first_name + second_name
print(full_name)

#Modifying string
sentence = 'the dog name is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# custom string formatting for
output ="Hello, " + first_name + " " + second_name
output = "Hello, {} {}".format(first_name, second_name)
output = "Hello, {0} {1}".format(full_name, second_name)

# Only available in python 3
#output = f'Hello, {first_name} {second_name}' 
print(output)

#converting types to strings
# 1. number to string 
days = 23
print(str(days) + " days in May")
# 2. string to number {we use float or int}
first_num = "5"
second_num = "6"
print(int(first_num) + float(second_num))

# More about numbers
f_num = input("Enter number one:")
s_num = input("Enter number two:")
print(int(f_num) ** int(s_num)) # converted to int because every input is treated as a string


