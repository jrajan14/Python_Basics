# Python Basics
# Functions

# Built-in functions
print("Hello, world!")
len([1, 2, 3, 4, 5])
max(10, 20, 30)

# A user-defined function
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)  # Output: Hello, Alice!


# Lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Higher-order function
def apply(func, x):
    return func(x)

def double(x):
    return x * 2

print(apply(double, 3))  # Output: 6

# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)  # Output: 5, 4, 3, 2, 1

# Decorator function
def uppercase_decorator(func):
    def wrapper(text):
        result = func(text)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))  # Output: HELLO, BOB!

# Method function
text = "Hello, world!"
print(text.upper())  # Output: HELLO, WORLD!

## Parameter Passing

# Positional Parameters
def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8

# Keyword Parameters
def greet(name, message):
    return f"Hello, {name}! {message}"

result = greet(message="How are you?", name="Alice")
print(result)  # Output: Hello, Alice! How are you?

# Default Parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Output: 9 (3^2)
print(power(2, 4))   # Output: 16 (2^4)

# Arbitrary Number of Parameters:
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3, 4))  # Output: 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Wonderland")
# Output:
# name: Alice
# age: 30
# city: Wonderland


# Unpacking Arguments
def multiply(x, y):
    return x * y

nums = (2, 3)
result = multiply(*nums)
print(result)  # Output: 6

# Passing Mutable Objects
def modify_list(lst):
    lst.append(4)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  
# Output: [1, 2, 3, 4]

