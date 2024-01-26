num=input('Enter a number from 0-6:')
match num:
    case '0':
        print('SUNDAY')
    case '1':
        print('MONDAY')    
    case '2':
        print('TUESDAY')
    case '3':
        print('WEDNESDAY')
    case '4':
        print('THURSDAY')
    case '5':
        print('FRIDAY')
    case '6':
        print('SATURDAY')
    case _:
        print('INVALID')
    