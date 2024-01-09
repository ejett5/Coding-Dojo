class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance, withdraw, deposit, yield_interest): 
        self.interest_rate = int_rate
        self.balance = balance
        self.withdraw = withdraw
        self.deposit = deposit
        self.yield_interest = yield_interest
        # self.user_name = user

    def deposit(self, amount):

        if(self.balance >= 0):
            self.balance += amount #TODO link the amount to an var input
        else:
            print("Please reach out to our representatives at: 555-555-5555")

# amount to be withdrawn and update bank balance
    def withdraw(self, withdraw_amount):

        if(self.balance >= 0):
            self.balance -= withdraw_amount
            print(self.balance)
        else:
            print("insufficient funds, your account will now be charged a $5 fee")

        
    def display_account_info(self):

        print(self.balance, self.interest_rate, self.yield_interest, self.deposit) 

        
    def yield_interest(self):

        self.interest_rate = self.interest_rate * self.balance
        
jm_toyota = BankAccount('18', '100', '20', '1', '3.5')
print(jm_toyota.display_account_info())
