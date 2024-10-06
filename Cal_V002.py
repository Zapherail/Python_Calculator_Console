#Cal_V002 - Basic math
# Changes from V-001: Changed the math to functions. Added while loop to continue calculations.
# Testing connection to Git

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num2 - num1

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


while True:
    num1 = int(input('What is the first number? '))
    num2 = int(input('What is the second number? '))
    op = input('What do you want to do? ')
    result = 0

    if op == 'add' or op == '+':
        result = add(num1, num2)
    elif op == 'subtract' or op == '-':
        result = subtract(num1, num2)
    elif op == 'multiply' or op == '*':
        result = multiply(num1, num2)
    elif op == 'divide' or op == '/':
        result = divide(num1, num2)
    else:
        print('Invalid choice')

    print(f'The result is: {result}')
    choice = input('Do you want to do it again (yes or no): ')

    if choice == 'n' or choice == 'no':
        break

