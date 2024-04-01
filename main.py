import random
import math
import os

# Print statement
print('Hello from main.py')

# Declaring variables
first_name = None
print(first_name)

first_name = 'George'
print(first_name)

last_name = 'Bush'
print(last_name)

# In Python, you don't redeclare variables. Just assign a new value.
last_name = 'Clinton'
print(f'{first_name} {last_name}')

# String literals
my_string1 = "This is a string"
my_string2 = 'This is also a string'
my_string3 = "John's string with an apostrophe"
my_string4 = 'John\'s string with an apostrophe'
my_string5 = 'My "string" in quotes'
my_string6 = "My \"string\" in quotes"

print(my_string1)
print(my_string2)
print(my_string3)
print(my_string4)
print(my_string5)
print(my_string6)

# String concatenation
full_name = first_name + ' ' + last_name
print(full_name)

# Accessing characters in a string
print(full_name[0])
print(full_name[7])

# Negative indexing is allowed in Python
print(full_name[-1])

# If the index is out of bounds, Python throws an IndexError
try:
    print(full_name[44])
except IndexError:
    print('Index out of bounds.')

# String methods
print(full_name.upper())
print(full_name.lower())

def title_case(string):
    return ' '.join(word.capitalize() for word in string.split(' '))

print(title_case('plEASe tiTLe CaSE tHis StrinG'))

# Finding the length of a string
print(len(full_name))

# Slicing strings
print(full_name[4:9])
print(full_name[4:])
print(full_name[16:])
print(full_name[-5:])

# Replacing substrings
print(full_name.replace('George', 'Bill'))

# Formatted strings (f-strings in Python)
multi_line_string = """This is a string
that is written
on multiple lines"""
print(multi_line_string)

funk_man = f'The best funk musician of his time was {full_name}'
print(funk_man)

char1 = "smart"
char2 = "funny"
char3 = "not as tall as me"

my_bff = f'My best friend is {char1}, {char2}, and {char3}'
print(my_bff)

# Clearing the console
os.system('cls' if os.name == 'nt' else 'clear')

# The `type` function in Python is equivalent to JavaScript's `typeof` operator
print(type('Hello'))
print(type(full_name))

# Numeric types and operations
some_int = 123
print(some_int)
print(type(some_int))

some_float = 3.14
print(some_float)
print(type(some_float))

sum_val = 10 + 5
print(sum_val)

# Other arithmetic operations
diff = 10 - 5
print(diff)

diff -= 2
print(diff)

diff -= 1
print(diff)

prod = 5 * 5
print(prod)

prod *= 5
print(prod)

quotient = 88 / 22
print(quotient)

quotient /= 8
print(quotient)

square = 5**2
print(square)

square **= 2
print(square)

mod = 37 % 8
print(mod)

mod %= 2
print(mod)

# Floor division and ceiling
floor = 5 // 2
print(floor)

ceil_value = math.ceil(5 / 2)
print(ceil_value)

# Type conversion
my_num = 123
my_other_num = '456'

added = my_num + int(my_other_num)
print(added)
print(type(added))

quiz1 = '10' + '9'
print(quiz1)

quiz2 = int('10') - int('9')
print(quiz2)

quiz3 = 10 > int('9')
print(quiz3)

quiz4 = '10' > '9'
print(quiz4)

quiz5 = 'S' > str(9)
print(quiz5)

# Boolean values
my_bool1 = True
print(my_bool1)
print(type(my_bool1))

my_bool2 = False
print(my_bool2)
print(type(my_bool2))

# Comparison operators
print(1 < 2)
print(1 > 2)
print(10 >= 10)
print(10 <= 5)
print(1 != 2)
print(1 == 2)

num_one = 1
str_one = '1'

print(num_one == int(str_one))

# Logical not operator
print(not True)
print(not False)

# If Statements
age = 100

if age > 18:
    print('You are eligible to vote')

if age >= 35:
    print('You are old enough to run for president')
else:
    print('You are too young to run for president')

age = 9

if age >= 65:
    print('You are a senior citizen')
elif age >= 18:
    print('You are an adult')
else:
    print('You are a child')

# While loops
my_random_number = random.randint(0, 9)
print('Starting random number:', my_random_number)

while my_random_number != 5:
    print(my_random_number)
    my_random_number = random.randint(0, 9)

print('Ending random number:', my_random_number)
