#print hello world
print("Hello World!")

# print the given name
name = "Mickey"
print( "Hello my name is: ", name) #with a comma
print( "My name is: " + name) #with a +

#print hello 42
name = 42
print( "The given name is: " + str(name))
print( "The given name of: ", str(name))

#print foods you love
fave_food1 = "chicken"
fave_food2 = "pizza"
print("Two of my favorite foods are {}, and {}.".format(fave_food1, fave_food2)) #use .format()
print(f"When I am hungry my protein of choice is usually {fave_food1}. Sometimes it is good to just enjoy what I want to eat so I willg eat {fave_food2}.") #use f string