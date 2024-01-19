import random
num=random.randint(100,1000)
while True:
    a=int(input('enter a number:'))
    if a==num:
        print('Congrats! You Won')
        break
    elif a<num:
        print('Enter Greater Number')
    else:
        print('Enter lesser Number')