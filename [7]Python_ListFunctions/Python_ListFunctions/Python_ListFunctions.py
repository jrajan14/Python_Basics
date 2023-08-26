
# Python Basics
# List Types and Functions

##################
# List of Integers
##################
int_list = [1, 2, 3, 4, 5]
print(int_list)

# List functions
length = len(int_list)
print("Length:", length)

sum_values = sum(int_list)
print("Sum:", sum_values)

max_value = max(int_list)
print("Max:", max_value)

min_value = min(int_list)
print("Min:", min_value)

sorted_list = sorted(int_list)
print("Sorted:", sorted_list)

#################
# List of Strings
#################
string_list = ["apple", "banana", "cherry", "date"]
print(string_list)

# List functions
length = len(string_list)
print("Length:", length)

sorted_list = sorted(string_list)
print("Sorted:", sorted_list)

joined_string = "-".join(string_list)
print("Joined:", joined_string)

##########################
# List of Mixed Data Types
##########################
mixed_list = [10, "hello", 3.14, True]
print(mixed_list)

# List functions
length = len(mixed_list)
print("Length:", length)

# List indexing
value = mixed_list[1]
print("Value at index 1:", value)

##############################
# List of LISTS (Nested Lists)
##############################
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)

# Accessing elements in a nested list
element = nested_list[1][2]
print("Element at (1, 2):", element)

################
# List Functions
################
numbers = [5, 2, 8, 1, 9]

# Adding elements
numbers.append(7)
print("After append:", numbers)

numbers.insert(2, 6)
print("After insert:", numbers)

# Removing elements
numbers.remove(8)
print("After remove:", numbers)

popped_value = numbers.pop()
print("Popped value:", popped_value)
print("After pop:", numbers)

# List comprehension
squared_numbers = [x ** 2 for x in numbers]
print("Squared numbers:", squared_numbers)

# Count occurrences
count_2 = numbers.count(2)
print("Count of 2:", count_2)

# Index of an element
index_9 = numbers.index(9)
print("Index of 9:", index_9)

# Reversing the list
numbers.reverse()
print("Reversed list:", numbers)

# Clearing the list
numbers.clear()
print("Cleared list:", numbers)
