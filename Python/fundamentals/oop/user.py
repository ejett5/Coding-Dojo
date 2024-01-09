

#making class for user arguments

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.age = age
        self.is_rewards_memeber = False
        self.gold_card_points = 0
        #display_info intended to print all user info
        # display_info(self)  ##assignment said to add this to the class but it is wrong as there is just an empty; changing levels has no effect and only adds erros
        #there is no parameter or arg for display_info(self) and returns undefined error
        
#making users and printing their data for display  
user_default_1 = User('John', 'Doe', 'fake123@email.com', '42')
print(user_default_1)