
# Python Basic Programs
# Datatypes in Python

##############################
# Boolean - bool (True, False)
##############################

x = True 
y = False
print("X is", x, ", Y is", y)

#######################################
# Binary - bytes, bytearray, memoryview
#######################################

# Creating a bytes object
binary_data = b'\x41\x42\x43\x44\x45'  # Bytes representing ASCII values 'A', 'B', 'C', 'D', 'E'
print("Bytes:", binary_data)

# Accessing individual bytes
first_byte = binary_data[0]
print("First Byte:", first_byte)

# Iterating through bytes
for byte in binary_data:
    print("Byte:", byte)

# Creating a bytearray
byte_array = bytearray(b'\x61\x62\x63\x64\x65')  # Bytes representing ASCII values 'a', 'b', 'c', 'd', 'e'
print("Bytearray:", byte_array)

# Modifying individual bytes in a bytearray
byte_array[0] = 0x66  # Setting the first byte to ASCII value 'f'
print("Modified Bytearray:", byte_array)

# Adding new bytes to a bytearray
byte_array.extend(b'\x67\x68')  # Adding bytes representing ASCII values 'g', 'h'
print("Extended Bytearray:", byte_array)

###############################
# Numeric - int, float, complex
###############################

integer_num = 42
negative_integer = -10
big_integer = 123456789012345678901234567890
print ("Integer: ", integer_num, ", Negative integer :", negative_integer, ", Big Integet : ", big_integer)

float_num = 3.14
negative_float = -0.001
scientific_notation = 2.5e3  # 2.5 * 10^3 or 2500
print ("Float : ", float_num, ", negative float : ",  negative_float, ", Scientific Notation : ", scientific_notation)

complex_num = 3 + 2j
negative_complex = -1 - 4j
print("Complex number : ", complex_num, ", Negative complex : ", negative_complex)

##############
# String - str
##############

single_quoted = 'Hello, world!'
double_quoted = "Python is fun!"
triple_quoted = '''This is a multi-line
string using triple quotes.'''

print(single_quoted)
print(double_quoted)
print(triple_quoted)

# Indexing and Slicing strings
my_string = "Hello, Python!"
first_char = my_string[0]
substring = my_string[7:13]
last_char = my_string[-1]

print(first_char)
print(substring)
print(last_char)

# String concat
greeting = "Hello"
name = "Bond, James Bond"
message = greeting + ", " + name + "!"

print(message)

# String formatting
age = 25
formatted_string = "I am {} years old.".format(age)
f_string = f"I am {age} years old."

print(formatted_string)
print(f_string)

# String Methods
text = "Python is amazing!"

lower_case = text.lower()
upper_case = text.upper()

substring_index = text.index("amazing")
contains_substring = "amazing" in text

words = text.split()
joined_string = "-".join(words)

text_with_spaces = "  This has extra spaces.   "
stripped_text = text_with_spaces.strip()

print(lower_case)
print(upper_case)
print(substring_index)
print(contains_substring)
print(words)
print(joined_string)
print(stripped_text)

# Escaping characters
escaped_string = "This is a \"quoted\" text."
new_line = "Line 1\nLine 2"
tabbed = "Column 1\tColumn 2"

print(escaped_string)
print(new_line)
print(tabbed)

# String length
message = "Hello, world!"
length = len(message)
print(length)

# Raw String
raw_string = r"C:\Users\username\Documents"
print(raw_string)


#################################
# Sequential - list, tuple, range
#################################

#LIST :  Lists are ordered, mutable collections of items.
fruits = ["apple", "banana", "orange", "grape"]

print("Fruits:", fruits)

second_fruit = fruits[1]
print("Second Fruit:", second_fruit)

fruits[2] = "kiwi"
print("Modified Fruits:", fruits)

fruits.append("pear")
print("Fruits after appending:", fruits)

removed_fruit = fruits.pop(1)
print("Removed Fruit:", removed_fruit)
print("Fruits after removing:", fruits)

selected_fruits = fruits[1:3]
print("Selected Fruits:", selected_fruits)

# TUPLES : Tuples are ordered, immutable collections of items.
coordinates = (3, 5)

print("Coordinates:", coordinates)

x = coordinates[0]
print("x-coordinate:", x)

x, y = coordinates
print("Unpacked Coordinates: x =", x, ", y =", y)

#RANGE : The range function generates a sequence of numbers.
numbers = range(5)
number_list = list(numbers)

print("Generated Range as List:", number_list)

custom_range = range(2, 10)
print("Custom Range:", list(custom_range))

stepped_range = range(1, 11, 2)
print("Stepped Range:", list(stepped_range))

###############
# Mapped - dict
###############

# Define a function to double a number
def double(x):             #Refer to PYTHON FUNCTIONS tutorial
    return x * 2

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map to apply the double function to each number in the list
doubled_numbers = map(double, numbers)

# Convert the result to a list (since map returns an iterator)
doubled_numbers_list = list(doubled_numbers)

print("Original Numbers:", numbers)
print("Doubled Numbers:", doubled_numbers_list)


######################
# Set - set, frozenset
######################

# Creating a set
fruits = {"apple", "banana", "orange", "apple"}  # Note: Duplicate "apple" is ignored

# Adding elements to a set
fruits.add("grape")
fruits.update(["kiwi", "mango"])

# Removing elements from a set
fruits.remove("banana")  # Raises an error if the element is not present
fruits.discard("apple")  # Removes the element if it's present, otherwise does nothing

# Set operations
vegetables = {"carrot", "spinach", "mango"}

# Union of two sets
combined = fruits.union(vegetables)

# Intersection of two sets
common_elements = fruits.intersection(vegetables)

# Difference between two sets
unique_to_fruits = fruits.difference(vegetables)

print("Fruits Set:", fruits)
print("Vegetables Set:", vegetables)
print("Combined Set:", combined)
print("Common Elements:", common_elements)
print("Unique to Fruits:", unique_to_fruits)

# Creating a frozenset
normal_set = {1, 2, 3}
frozen = frozenset(normal_set)
# Trying to modify a frozenset (this will raise an error)
try:
    frozen.add(4)
except AttributeError as e:
    print("Error:", e)

# Operations with frozensets
frozen_a = frozenset({1, 2, 3})
frozen_b = frozenset({2, 3, 4})

# Intersection of two frozensets
intersection = frozen_a.intersection(frozen_b)

# Union of two frozensets
union = frozen_a.union(frozen_b)

# Difference between two frozensets
difference = frozen_a.difference(frozen_b)

print("Original Set:", normal_set)
print("Frozen Set:", frozen)
print("Intersection:", intersection)
print("Union:", union)
print("Difference:", difference)

#################
# None - NoneType
#################

# Function that doesn't return a value explicitly
def print_message(message):
    print(message)

result = print_message("GAME OVER!")

print("Result:", result)  # Output: Result: None
