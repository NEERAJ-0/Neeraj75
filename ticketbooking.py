print('\nWelcome to NK Travels online Booking')
print('select the Destination from below')
d=eval(input('1-BNG>CHENNAI(350km)\n2-BNG>MUMBAI(800km)\n3-BNG>DELHI(2000km)\n4-BNG>HYDERABAD(500km)\n'))
if d==1:
    print('BANGLORE-CHENNAI')
    ad=eval(input('Enter no of ADULTS:'))
    ch=eval(input('Enter no of CHILDREN:'))
    ac=eval(input('select Coach\n1-A/C\n2-NON-A/C\n'))
    if ac==1:
        c=ad*10*350
        a=ch*5*350
        print('________________________')
        print('ADULTS',ad,'=',c,sep='  ')
        print('CHILDREN',ch,'=',a,sep='  ')
        print('Total no.of Seats:',ad+ch)
        t=a+c
        print('TOTAL PRICE=',t)
        print('TICKETS BOOKED')
        print('HAPPY JOURNEY!')
    elif ac==2:
        c=ad*5*350
        a=ch*3*350
        print('________________________')
        print('ADULTS',ad,'=',c,sep='  ')
        print('CHILDREN',ch,'=',a,sep='  ')
        print('Total no.of Seats:',ad+ch)
        t=a+c
        print('TOTAL PRICE=',t)
        print('TICKETS BOOKED')
        print('HAPPY JOURNEY!')
    else:
        print('enter valid coach')
elif d==2:
    print('BANGLORE-MUMBAI') 
    ad=eval(input('Enter no of ADULTS:'))
    ch=eval(input('Enter no of CHILDREN:'))
    ac=eval(input('select Coach\n1-A/C\n2-NON-A/C\n'))
    if ac==1:
        c=ad*10*800
        a=ch*5*800
        print('________________________')
        print('ADULTS',ad,'=',c,sep='  ')
        print('CHILDREN',ch,'=',a,sep='  ')
        print('Total no.of Seats:',ad+ch)
        t=a+c
        print('TOTAL PRICE=',t)
        print('TICKETS BOOKED')
        print('HAPPY JOURNEY!')
    elif ac==2:
        c=ad*5*800
        a=ch*3*800
        print('________________________')
        print('ADULTS',ad,'=',c,sep='  ')
        print('CHILDREN',ch,'=',a,sep='  ')
        print('Total no.of Seats:',ad+ch)
        t=a+c
        print('TOTAL PRICE=',t)
        print('TICKETS BOOKED')
        print('HAPPY JOURNEY!')
    else:
        print('enter valid coach')
elif d==3:
    print('BANGLORE-DELHI')
    ad=eval(input('Enter no of ADULTS:'))
    ch=eval(input('Enter no of CHILDREN:'))
    ac=eval(input('select Coach\n1-A/C\n2-NON-A/C\n'))
    if ac==1:
        c=ad*10*2000
        a=ch*5*2000
        print('________________________')
        print('ADULTS',ad,'=',c,sep='  ')
        print('CHILDREN',ch,'=',a,sep='  ')
        print('Total no.of Seats:',ad+ch)
        t=a+c
        print('TOTAL PRICE=',t)
        print('TICKETS BOOKED')
        print('HAPPY JOURNEY!')
    elif ac==2:
        c=ad*5*2000
        a=ch*3*2000
        print('________________________')
        print('ADULTS',ad,'=',c,sep='  ')
        print('CHILDREN',ch,'=',a,sep='  ')
        print('Total no.of Seats:',ad+ch)
        t=a+c
        print('TOTAL PRICE=',t)
        print('TICKETS BOOKED')
        print('HAPPY JOURNEY!')
    else:
        print('enter valid coach')
elif d==4:
    print('BANGLORE-HYDERABAD')
    ad=eval(input('Enter no of ADULTS:'))
    ch=eval(input('Enter no of CHILDREN:'))
    ac=eval(input('select Coach\n1-A/C\n2-NON-A/C\n'))
    if ac==1:
        c=ad*10*500
        a=ch*5*500
        print('________________________')
        print('ADULTS',ad,'=',c,sep='  ')
        print('CHILDREN',ch,'=',a,sep='  ')
        print('Total no.of Seats:',ad+ch)
        t=a+c
        print('TOTAL PRICE=',t)
        print('TICKETS BOOKED')
        print('HAPPY JOURNEY!')
    elif ac==2:
        c=ad*5*500
        a=ch*3*500
        print('________________________')
        print('ADULTS',ad,'=',c,sep='  ')
        print('CHILDREN',ch,'=',a,sep='  ')
        print('Total no.of Seats:',ad+ch)
        t=a+c
        print('TOTAL PRICE=',t)
        print('TICKETS BOOKED')
        print('HAPPY JOURNEY!')
    else:
        print('enter valid coach')
else:
    print('choose right destination')


