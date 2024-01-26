num1=int(input('Enter a number1:'))
num2=int(input('Enter a number2:'))
optr=input('Enter a operator:')
match optr:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)    
    case '/':
        print(num1/num2)
    case '%':
        print(num1%num2)
    case '//':
        print(num1//num2)
    case '*':
        print(num1*num2)
    case '**':
        print(num1**num2)
    case _:
        print('INVALID OPERATOR')
    