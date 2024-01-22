print('\nWelcome to NK Travels online Booking')
print('____________________________________')
dest=input('''select the Destination from below
    1-CHENNAI(350km)
    2-MUMBAI(800km)
    3-DELHI(2000km)
    4-HYDERABAD(500km)\n''')
adult_seats=int(input('Enter no of ADULTS:'))
child_seats=int(input('Enter no of CHILDREN:'))
coach=input('select Coach\n1-A/C\n2-NON-A/C\n')
distance={'1':350,'2':800,'3':2000,'4':500}
if coach=='1':
    adult_price=3
    child_price=2   
elif coach=='2':
    adult_price=2
    child_price=1
total_price=distance[dest]*(adult_price*adult_seats+child_price*child_seats)
print('The total amount is',total_price,'/-')
confirm=input('Are you confirm to Book!\n1.Yes 2.No\n')
if confirm=='1':
    print('Tickets Booked successfully...')
    print('HAPPY JOURNEY...!')    
else:
    print('Your Transaction is Cancelled...!')