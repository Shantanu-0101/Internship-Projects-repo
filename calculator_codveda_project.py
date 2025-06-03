def calculator(num1,num2):
    if  operation == '+':
        print(f'{num1} + {num2} = ', num1 + num2)
    
    elif operation == '-':
        print(f'{num1} - {num2} = ', num1 - num2)

    elif operation == '*':
        print(f'{num1} * {num2} = ', num1 * num2)

    elif operation == '/':
        if num2 == 0:
            raise Exception('Cant divide by zero')
        else:
            print(f'{num1} / {num2} = ', num1 / num2)

num1 = int(input("Enter First Number :"))

operation = (input("Select an operation = '+', '-', '*', '/' : "))

num2 = int(input("Enter Second Numer :"))


calculator(num1,num2)

