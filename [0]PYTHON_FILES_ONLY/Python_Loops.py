
# Python Basic Programs
# Loops in Python

##########
# FOR LOOP
##########
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

############
# WHILE LOOP
############
count = 0

while count < 5:
    print("Count:", count)
    count += 1

#############
# NESTED LOOP
#############
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

##############################
# LOOPING THROUGH A DICTIONARY
##############################
person = {"name": "Alice", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")

##########################
# LOOPING WITH 'enumerate'
##########################
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

######################
# LOOPING WITH 'range'
######################
for num in range(5):
    print(num)

##############################################
# LOOP CONTROL STATEMENTS (break and continue)
##############################################
for num in range(10):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)

for num in range(5):
    if num == 2:
        continue  # Skip the rest of the loop for num equal to 2
    print(num)

############################
# LOOPING WITH 'else' CLAUSE
############################
for num in range(5):
    print(num)
else:
    print("Loop completed without using break")
