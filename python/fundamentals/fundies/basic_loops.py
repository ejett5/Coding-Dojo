#print num 0 to 150 inclusive
n = 0
while n <= 150:
    print(n)
    n += 1

#print multiples of 5 from 5 to 1,000
# fives = 0
# while fives <= 1000:
#     if fives % 5:  # need to revist to logic of what is wanted
#         print(fives)
#         fives += 5


# counting dojo way

n = 0
for n in range(0, 1001):
    #divisible by 5
    if n % 10 == 0:
        print("Dojo Way")
        n += 1
    #divisible by 10
    elif n % 5 == 0:
        print("Coding")
        n += 1
    #anything not divisible by 5 or 10
    else:
        print(n)
        n += 1

# #add odd int from 0 to half million then print the final sum (looked up basic py logic for start and end points)

def sum_odd(): #thank you vince for help with the syntax issues
    final = 0
    for num in range(5, 500000):
        if num % 2 == 1:
            final += num
    return final        
        
print(sum_odd())


# count down by 4
n = 2018
while n >=0:
    print(n)
    n -= 4

#flexi counter with low, high and mult values.
low_num = 2
high_num = 9
multi = 3

for n in range( low_num, high_num +1):
    if n % multi == 0:
        print(n)
        
