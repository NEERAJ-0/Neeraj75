class  Bank:
    #Bank details
    bank_name='HDFC BANK LTD'
    manager='Mr.Neeraj'
    ifsc='HDFC000532'
    branch='Palamaner'

    #Account details
    def __init__(self,n,an,m,b):
        self.name=n
        self.acc_no=an
        self.mobile=m
        self.balance=b

    #Transactions
    def credit(self,cr_amount):
        self.balance+=cr_amount
        print(cr_amount,' Credited Successfully...')

    def debit(self,dr_amount):
        if dr_amount<self.balance:
            self.balance-=dr_amount
            print(dr_amount,' Debited fom Your Account!')
        else:
            print('Insufficient Amount!')
        
    def sendmoney(self,transfer_amt,recipient_name):
        if transfer_amt>0  and  transfer_amt<=self.balance:
                if recipient_name!=self.acc_no:
                    self.balance-=transfer_amt
                    recipient=None
                    for acc in ['ram','sita','arjun','krishna']:
                        if recipient_name==acc:
                            recipient=acc
                            break
                    if recipient:
                        recipient.balance+=transfer_amt
                        print(f'{transfer_amt} Transferred to A/C.No:{recipient_name} Successfully...')
                    else:
                        print('Invalid Account No!')
                else:
                    print("Can't Transfer to Same Account")
        else:
            return 'Insufficient Amount'

    #changes in Accounts    
    def update_mob(self,new):
        self.mobile=new
        print('Mobile No updated successfully...')

    #Changes in Bank
    @classmethod
    def appoint(cls,mg):
        cls.manager=mg
        print('->New Manager Appointed')

    def change_ifsc(cls,ni):
        cls.ifsc=ni
        print('IFSC Code changed..!')
    

ram=Bank('Ram',5320001,7959253767,20000)
sita=Bank('Sita',5320002,9949658153,5000)
arjun=Bank('Arjun',5320003,8549770422,10000)
krishna=Bank('Krishna',5320004,7943408561,50000)
