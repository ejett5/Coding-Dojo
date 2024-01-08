
# x = [ [5,2,3], [10,8,9] ] 
# #change 10 to 5
# x[1][0] = 5
# print(x)
# print(x[1])# bonus from typing answer here instead of chat


# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# #change last name from Jordan to Bryant
# students[1]['last_name'] = 'Bryant'
# print(students)



# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# #messi becomes Andres
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# z = [ {'x': 10, 'y': 20} ]
# #20 to 30
# z[0]['y'] = 30
# print(z)


# #section 2 for iterating through dictionary
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# print(students)
def iterate_dictionary(key_name, students, value_name):
    for student in students:
        # for key, val in students: #not needed used for inner list
        #     print(f'{key} + {val}')
        print(student[key_name] +" " + student[value_name])
iterate_dictionary('first_name', students, 'last_name')
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel
