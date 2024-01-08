
x = [ [5,2,3], [10,8,9] ] 
#change 10 to 5
x[1][0] = 5
print(x)


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#change last name from Jordan to Bryant
students[1]['last_name'] = 'Bryant'
print(students)



sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
#messi becomes Andres
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
#20 to 30
z[0]['y'] = 30
print(z)
