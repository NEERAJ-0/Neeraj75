def prime(num):
    flag=False
    if isinstance(num,int) and num>1:
        for i in range(2,num):
            if num%i==0:
                flag=True
                break
        if flag:
            print('not a prime')
        else:
            print('prime')
    else:
        print('Invalid Argument')
