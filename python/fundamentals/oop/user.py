

#making class for user arguments

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.spend_rewards_points = self.gold_card_points #- 80
        #display_info intended to print all user info
    def display_info(self):
        print(self.first, self.last, self.email, self.age, self.is_rewards_member, self.gold_card_points )
#allow person to enroll as member and set status to True
    def enroll_self(self):
        self.is_rewards_member = True
# tracking how many points are spent      
    def spend_points(self, amount):  
        self.gold_card_points -=  amount


        
#making users and printing their data for display  
user_default_1 = User('John', 'Doe', 'fake123@email.com', '42')
# print(user_default_1.display_info())
user_default_1.is_rewards_member = True #changing to rewards memeber
user_default_1.gold_card_points = 200
# print(user_default_1.display_info()) #showing change in memeber status
user_default_1.spend_points(50)  #arg in funct will activate the funct created earlier and then run with the value placed in
print(user_default_1.display_info())

#creating another instance of user
user_Sally = User('Sally', 'Ride', 'first2space@nasa.net', '61')
# print(user_Sally.display_info())
user_Sally.spend_points(80)
print(user_Sally.display_info)

#make second user
billy_mitchell = User('Billy','Mitchell', 'brigadiergen@USAF.net', '56')
# print(billy_mitchell.display_info())
billy_mitchell.gold_card_points = 999999
billy_mitchell.is_rewards_member = True
print(billy_mitchell.display_info())