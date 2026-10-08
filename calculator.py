




while True:

    print('Write an expression')
    expression = input()
    expression = expression.replace(' ','')
    if any(operator in expression for operator in ['+','-','*','/']):
        for operator in expression:
            if operator in ['+','-','*','/']:
                expression = expression.split(operator)
                op = operator

        if len(expression) == 2:
            try:
                num1 = float(expression[0])
                num2 = float(expression[1])
                break
            except ValueError:
                print('You may only input numbers!')
        elif len(expression) < 2:
            print('Your expression is too short!')
        else:
            print('Your expression is too long!')
    else:
        print('Your input does not contain a supportable operators: "+", "-", "*", "/"')

match op:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = 'undefined'

print(f'The result is: {result}')