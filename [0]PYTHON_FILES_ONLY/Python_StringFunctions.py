# Python Basics
# String Functions

# SImple String Declaration
text = "Hello World..."

# Length of a String
length = len(text)
print("Length:", length)

# Convert to Lowercase and Uppercase
lowercase_text = text.lower()
uppercase_text = text.upper()
print("Lowercase:", lowercase_text)
print("Uppercase:", uppercase_text)

# Capitalize the First Letter
capitalized_text = text.capitalize()
print("Capitalized:", capitalized_text)

# Title Case (Capitalize each Word)
title_text = text.title()
print("Title Case:", title_text)

# Count Occurrences of a Substring
count_e = text.count("e")
print("Count of 'e':", count_e)

# Find The Index of a Substring (or -1 if Not Found)
index_world = text.find("World")
print("Index of 'World':", index_world)

# Replace a Substring
new_text = text.replace("Hello", "Hi")
print("Replaced text:", new_text)

# Check if The String Starts or Ends with a Given Substring
starts_with_hello = text.startswith("Hello")
ends_with_exclamation = text.endswith("!")
print("Starts with 'Hello':", starts_with_hello)
print("Ends with '!':", ends_with_exclamation)

# Remove Leading and Trailing Whitespace
whitespace_text = "   This has whitespace.   "
stripped_text = whitespace_text.strip()
print("Stripped text:", stripped_text)

# Split a String Into a List of Substrings
words = text.split(", ")
print("Split words:", words)

# Join a List of Strings Into a Single String
joined_text = "-".join(words)
print("Joined text:", joined_text)

# Formatting Strings
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I'm {age} years old."
print("Formatted string:", formatted_string)

# String Slicing
substring = text[7:12]
print("Substring:", substring)
