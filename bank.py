class  Bank:
    #Bank details
    bank_name = 'HDFC BANK LTD'
    manager   = 'Mr.Neeraj'
    ifsc      = 'HDFC000532'
    branch    = 'Palamaner'

    #Account info
    def __init__(self, n, an, m, b):
        self.name    = n
        self.acct_no = an
        self.mobile  = m
        self.balance = b
        
    #credit
    def deposit(self, cr_amount):
        self.balance += cr_amount                         
        print(cr_amount, ' Credited to your Account Successfully...')
        print('Balance :',self.balance)

    #debit
    def withdraw(self, dr_amount):
        if dr_amount <= self.balance:                      
            self.balance -= dr_amount
            print(dr_amount, ' Debited fom Your Account!')
            print('Balance :',self.balance)
        else:
            print('Insufficient Amount!')
        
    #transfer to other Account    
    def transfer(self, transfer_amt, recipient):
        if  0 < transfer_amt <= self.balance:
            if recipient != self:
                self.balance      -= transfer_amt            
                recipient.balance += transfer_amt
                print(f'{transfer_amt} Transferred to {recipient.name} Successfully...')
            else:
                print("Can't Transfer to Same Account")
        else:
            print('Insufficient Amount')

    #change of Mobile.No    
    def update_mob(self, new):
        self.mobile = new
        print('Mobile No updated Successfully...')

    #Changes in Bank
    @classmethod
    def appoint(cls, mg):
        cls.manager = mg
        print('New Manager Appointed')

    @classmethod
    def change_ifsc(cls, ni):
        cls.ifsc = ni
        print('New IFSC Code:', ni)
    
    #Account details
    @staticmethod
    def account(acn):
        print(f'Details of {acn.name}',acn.bank_name,acn.ifsc,acn.branch,acn.name,
              acn.acct_no,acn.mobile,acn.balance,sep='\n')

    #Calculate Interest
    @staticmethod
    def interest(acct):
        interest_amount = (5.0 / 100) * acct.balance
        print(f"Interest for {acct.name}'s account: {interest_amount}")

krishna = Bank('Krishna',5320001,7943408561,50000)
radha   = Bank('Radha',5320002,8549770422,10000)
ram     = Bank('Ram',5320003,7959253767,25000)
sita    = Bank('Sita',5320004,9949658153,8000)
siri    = Bank('Siri',5320005,6304258855,0)
