numbers_t = (4,6,3,1,8,7) #immutable

numbers_l = [1,2,3] #mutable

a_t = numbers_t[0]

a_n = numbers_l[0]

numbers_l[1] = 5

#Gives an error because tuple is immutable 
# numbers_t[1] = 5

for number in numbers_t:
    print(number)
    
new_tuple = numbers_t[:]

new_list = list(numbers_t)

# numbers_t.append(9) You can't use append() in tuples.
# print(numbers_t)

# del numbers_t[1]  You can't delete item in tuples.
# print(numbers_t)