# print("Hello World!")

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance, withdraw, deposit, yield_interest): 
        self.interest_rate = int_rate
        self.balance = balance
        self.withdraw = withdraw
        self.deposit = deposit
        self.yield_interest = yield_interest
        # self.amount = amount
        # self.user_name = user
        # print()

    def deposit(self, deposit):
        
        if(self.balance >= 0):
            self.balance += deposit #TODO link the amount to update balance
            # print(self.balance)
        else: 
            print("Please reach out to our representatives at: 555-555-5555")

# amount to be withdrawn and update bank balance
    def withdraw(self, withdraw_amount):

        if(self.balance >= 0):
            self.balance -= withdraw_amount
            print(self.balance)
        else:
            print("insufficient funds, your account will now be charged a $5 fee")

    
    def yield_interest(self):

        self.interest_rate = self.interest_rate * self.balance

    def display_account_info(self):

        print(self.interest_rate, self.balance,self.withdraw, self.deposit, self.yield_interest) 
        return ""  #interpeter is taking this as another print but will show none or 0 without an empty return TODO figure out why it is reading it this way
        
jm_toyota = BankAccount(18, 100, 20, 1, 3.5)  #made as strings to test and made no difference on call
jack_black = BankAccount(3, 55, 100, 80, 3)
pedro_pascal = BankAccount(180, 1, 400, 142, 10) #TODO figure out why this stop functioning from col 39 on
print(jm_toyota.display_account_info(), jack_black.display_account_info(), pedro_pascal.display_account_info())

#updating info to user accounts
jm_toyota.deposit() == 50
# jm_toyota.deposit() == 50
print(jm_toyota.display_account_info()) #adding this section of code causes the pedro_pascal to have issues printing from the deposit att


# print(f"jm_toyota.display_account_info() + jack_black.display_account_info(), pedro_pascal.display_account_info()")  #just playing around to see if f string can be pushed in and combine multiples
# jm_toyota.withdraw(200).yield_interest_rate(5).display_account_info()  #TODO why is int not callable?
# jack_black.deposit(55).deposit(50).withdraw(1).withdraw(1).withdraw(1).withdraw(1).display_account_info()  #TODO why is int not callable?
# pedro_pascal.withdraw(200).yield_interest_rate(5).display_account_info()  #TODO why is int not callable?
