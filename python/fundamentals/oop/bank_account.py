# print("Hello World!")

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.interest_rate = int_rate
        self.balance = balance
        # self.amount = amount
        # self.user_name = user
        # print()

    def deposit(self, deposit):
        
        self.balance += deposit 
        print(f"current balance {self.balance}")
        return self
    
        

# amount to be withdrawn and update bank balance
    def withdraw(self, withdraw_amount):

        if(self.balance >= 0):
            self.balance -= withdraw_amount
            print(self.balance)
            return self 
        else:
            print("insufficient funds, your account will now be charged a $5 fee")
            return self

    
    def yield_interest(self):

        self.interest_rate = self.interest_rate * self.balance
        return self()

    def display_account_info(self):

        print(self.interest_rate, self.balance) 
        return self   #interpeter is taking this as another print but will show none or 0 without an empty return TODO figure out why it is reading it this way
    
    # class __init__(BankAccount):
    #     def super__init__(self):
    #         super().__init__()
    #         self.make_deposit = make_deposit
    #         return self()

        
jm_toyota = BankAccount(18, 100)  #made as strings to test and made no difference on call
jack_black = BankAccount(3, 55)
pedro_pascal = BankAccount(180, 1) 
jm_toyota.display_account_info(), jack_black.display_account_info(), pedro_pascal.display_account_info()

#updating info to user accounts
jm_toyota.deposit(50).deposit(50).display_account_info()
# jm_toyota.deposit(50)
jm_toyota.display_account_info() #adding this section of code causes the pedro_pascal to have issues printing from the deposit att


# print(f"jm_toyota.display_account_info() + jack_black.display_account_info(), pedro_pascal.display_account_info()")  #just playing around to see if f string can be pushed in and combine multiples
# jm_toyota.withdraw(200).yield_interest_rate(5).display_account_info()  #TODO why is int not callable?
# jack_black.deposit(55).deposit(50).withdraw(1).withdraw(1).withdraw(1).withdraw(1).display_account_info()  #TODO why is int not callable?
# pedro_pascal.withdraw(200).yield_interest_rate(5).display_account_info()  #TODO why is int not callable?
