import random
import math
import os

# Print statement
print('Hello from main.py')  # Output: Hello from main.py

# Declaring variables
first_name = None
print(first_name)  # Output: None

first_name = 'George'
print(first_name)  # Output: George

last_name = 'Bush'
print(last_name)  # Output: Bush

# In Python, you don't redeclare variables. Just assign a new value.
last_name = 'Clinton'
print(f'{first_name} {last_name}')  # Output: George Clinton

# String literals
my_string1 = "This is a string"
my_string2 = 'This is also a string'
my_string3 = "John's string with an apostrophe"
my_string4 = 'John\'s string with an apostrophe'
my_string5 = 'My "string" in quotes'
my_string6 = "My \"string\" in quotes"

print(my_string1)  # Output: This is a string
print(my_string2)  # Output: This is also a string
print(my_string3)  # Output: John's string with an apostrophe
print(my_string4)  # Output: John's string with an apostrophe
print(my_string5)  # Output: My "string" in quotes
print(my_string6)  # Output: My "string" in quotes

# String concatenation
full_name = first_name + ' ' + last_name
print(full_name)  # Output: George Clinton

# Accessing characters in a string
print(full_name[0])  # Output: G
print(full_name[7])  # Output: C

# Negative indexing is allowed in Python
print(full_name[-1])  # Output: n

# If the index is out of bounds, Python throws an IndexError
try:
    print(full_name[44])
except IndexError:
    print('Index out of bounds.')  # Output: Index out of bounds.

# String methods
print(full_name.upper())  # Output: GEORGE CLINTON
print(full_name.lower())  # Output: george clinton

def title_case(string):
    return ' '.join(word.capitalize() for word in string.split(' '))

print(title_case('plEASe tiTLe CaSE tHis StrinG'))  # Output: Please Title Case This String

# Finding the length of a string
print(len(full_name))  # Output: 14 (assuming last name is Clinton)

# Slicing strings
print(full_name[4:9])  # Output: ge Cl
print(full_name[4:])  # Output: ge Clinton
print(full_name[16:])  # Output: (empty string)
print(full_name[-5:])  # Output: inton

# Replacing substrings
print(full_name.replace('George', 'Bill'))  # Output: Bill Clinton

# Formatted strings (f-strings in Python)
multi_line_string = """This is a string
that is written
on multiple lines"""
print(multi_line_string)  # Output: This is a string
                           #         that is written
                           #         on multiple lines

funk_man = f'The best funk musician of his time was {full_name}'
print(funk_man)  # Output: The best funk musician of his time was George Clinton

char1 = "smart"
char2 = "funny"
char3 = "not as tall as me"

my_bff = f'My best friend is {char1}, {char2}, and {char3}'
print(my_bff)  # Output: My best friend is smart, funny, and not as tall as me

# Clearing the console is an action, no output to comment

# The `type` function in Python is equivalent to JavaScript's `typeof` operator
print(type('Hello'))  # Output: <class 'str'>
print(type(full_name))  # Output: <class 'str'>

# Numeric types and operations
some_int = 123
print(some_int)  # Output: 123
print(type(some_int))  # Output: <class 'int'>

some_float = 3.14
print(some_float)  # Output: 3.14
print(type(some_float))  # Output: <class 'float'>

sum_val = 10 + 5
print(sum_val)  # Output: 15

# Other arithmetic operations
diff = 10 - 5
print(diff)  # Output: 5

diff -= 2
print(diff)  # Output: 3

diff -= 1
print(diff)  # Output: 2

prod = 5 * 5
print(prod)  # Output: 25

prod *= 5
print(prod)  # Output: 125

quotient = 88 / 22
print(quotient)  # Output: 4.0

quotient /= 8
print(quotient)  # Output: 0.5

square = 5**2
print(square)  # Output: 25

square **= 2
print(square)  # Output: 625

mod = 37 % 8
print(mod)  # Output: 5

mod %= 2
print(mod)  # Output: 1

# Floor division and ceiling
floor = 5 // 2
print(floor)  # Output: 2

ceil_value = math.ceil(5 / 2)
print(ceil_value)  # Output: 3

# Type conversion
my_num = 123
my_other_num = '456'

added = my_num + int(my_other_num)
print(added)  # Output: 579
print(type(added))  # Output: <class 'int'>

quiz1 = '10' + '9'
print(quiz1)  # Output: 109

quiz2 = int('10') - int('9')
print(quiz2)  # Output: 1

quiz3 = 10 > int('9')
print(quiz3)  # Output: True

quiz4 = '10' > '9'
print(quiz4)  # Output: True

quiz5 = 'S' > str(9)
print(quiz5)  # Output: True

# Boolean values
my_bool1 = True
print(my_bool1)  # Output: True
print(type(my_bool1))  # Output: <class 'bool'>

my_bool2 = False
print(my_bool2)  # Output: False
print(type(my_bool2))  # Output: <class 'bool'>

# Comparison operators
print(1 < 2)  # Output: True
print(1 > 2)  # Output: False
print(10 >= 10)  # Output: True
print(10 <= 5)  # Output: False
print(1 != 2)  # Output: True
print(1 == 2)  # Output: False

num_one = 1
str_one = '1'

print(num_one == int(str_one))  # Output: True

# Logical not operator
print(not True)  # Output: False
print(not False)  # Output: True

# If Statements
age = 100

if age > 18:
    print('You are eligible to vote')  # Output: You are eligible to vote

if age >= 35:
    print('You are old enough to run for president')  # Output: You are old enough to run for president
else:
    print('You are too young to run for president')

age = 9

if age >= 65:
    print('You are a senior citizen')
elif age >= 18:
    print('You are an adult')
else:
    print('You are a child')  # Output: You are a child

# While loops
my_random_number = random.randint(0, 9)
print('Starting random number:', my_random_number)  # Output: Starting random number: [Random number]

while my_random_number != 5:
    print(my_random_number)  # Output: [Random number] (repeated until a 5 is generated)
    my_random_number = random.randint(0, 9)

print('Ending random number:', my_random_number)  # Output: Ending random number: 5
