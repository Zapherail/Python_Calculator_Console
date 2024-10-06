#Cal_V001 - Basic math

num1 = int(input('What is the first number? '))
num2 = int(input('What is the second number? '))
op = input('What do you want to do? ')
result = 0

if op == 'add' or op == '+':
    result = num1 + num2
elif op == 'subtract' or op == '-':
    result = num2 - num1
elif op == 'multiply' or op == '*':
    result = num1 * num2
elif op == 'divide' or op == '/':
    result = num1 / num2
else:
    print('Invalid choice')

print(f'The result is: {result}')