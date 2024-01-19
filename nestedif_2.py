a=eval(input('enter percentage\n'))
if a<35 and a>=0:
    print('FAIL')
elif a>=35 and a<50:
    print('PASS')
elif a<=100 and a>90:
    print('A+')
elif a<=90 and a>80:
    print('A')
elif a<=80 and a>70:
    print('B+')
elif a<=70 and a>60:
    print('B')
elif a<=60 and a>50:
    print('C')    
else:
    print('invalid marks')

