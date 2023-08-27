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
