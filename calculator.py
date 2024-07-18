num1 = int(input('First Number: '))

while True:
    operator = input('Operator (+, -, *, /): ')

    if operator in ['+', '-', '*', '/']:
        break
    else:
        print('Error: Choose one of the operators (+, -, *, /) ')

num2 = int(input('Second Number: '))

if operator == '+':
    print(num1 + num2)

elif operator == '-':
    print(num1 - num2)

elif operator == '*':
    print(num1 * num2)

elif operator == '/':
    print(num1 / num2)        

else:
    print('wrong operator. try again!')