print("Shree Ganesha, Hello python")

# DATA TYPES
# there 4 basic datatypes in python
# 1. int    - integer, which store whole numbers
# 2. float  - floating point number, which store decimal numbers
# 3. str    - string, which store text
# 4. bool   - boolean, which store True or False (first latter should be capital)

# VARIABLES
# Variables are used to store values in memory
# Variables are created when you assign a value to it
# Variables names are case-sensitive
# Variables names must start with a letter or underscore
# Variables names can contain letters, numbers, and underscores
name = "python1"
Name = "Rahul" # Name is different from name as python is case-sensitive
version = 3.8
is_interpreted = True


# OPERATORS | CONDITIONAL STATEMENTS
print("whats your name?")
name = input()
print("Hello ", name + ", To perform basic math operations, please enter two numbers")
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
operation = int(input("Enter [ 1 | 2 | 3 | 4 ], For [+ | - | * | /] operation respectively : "))
if operation == 1:
    print("Addition of ", num1, " and ", num2, " is ", num1 + num2)
if operation == 2:
    print("Subtraction of ", num1, " and ", num2, " is ", num1 - num2)
if operation == 3:
    print("Multiplication of ", num1, " and ", num2, " is ", num1 * num2)
if operation == 4:
    print("Division of ", num1, " and ", num2, " is ", num1 / num2) # division will alwasys return float value


# nested if-else
if name == "python":
    if Name == "Rahul":
        print("Hello ", Name, ", Welcome to python")
    else:
        print("Hello ", name)
else:
    print("Else block")


# LOOPS
# for loop
    # range(start, end, step) - step is the increment value
    # range(start, end) - step is 1 by default
    # range(end) - start is 0 by default

for i in range(0, 10, 2):
    print(i)

# while loop
while Name == "Rahul":
    print("Hello ", Name)
    break # break statement is used to exit the loop

while Name == "Rahul":
    print("Hello ", Name)
    Name = "jat"  # Name is not equal to "Rahul" so loop will be terminated