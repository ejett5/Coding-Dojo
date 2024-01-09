class User:
    def __init__(self, first_name, last_name, extra):
        self.first = first_name
        self.last = last_name
        self.extra = extra
        self.exercise = True 

# class User:
#     def __init__(self):
#         self.first_name = "Mickey"
#         self.last_name = "Jett"
#         self.extra = " Uses a dip pen"
#         self.exercise = True

# class User:
#     def __init__(self):
#         self.first_name = "John"
#         self.last_name = "Bob"
#         self.extra = " is super tall and slender and exclusively wears black suits"
#         self.exercise = True

user_mickey = User("Mickey","Jett", "Uses a dip pen")
user_john = User("John", "Bob", "is super tall and slender and exclusively wears black suits!")
# print(f'{user_mickey.first_name}{user_mickey.extra}')
# print(f'{user_john.first_name}{user_john.extra}')
print(user_mickey.first, user_mickey.extra)
print(user_john.first, user_john.extra)
