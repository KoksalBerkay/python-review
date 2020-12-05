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

################################################################
################### TUPLE RECAP ################################
################################################################

empty_tuple = ()

countries = ('Belgium', 'Germany', 'France', 'Netherland', 'Poland')
print(countries)

birthyears = (1985, 1986, 1988, 1989, 1999)
print(birthyears)

that_man = (42, 'smart', 1.70, True, ['tennis', 'walking', 'ski'])
print(that_man)

sport = that_man[4][0]
print(sport)

print('I like', sport)

print(countries[1:3])

# print(countries[3:])

print(countries[::-1])


# Below code gives us an error.
# countries[-1] = 'Hi'

# I can change whole tuple
countries = ('Spain', 'Sweden', 'Italy', 'Denmark', 'Norway')

check_if_exist = 'Belgium' in countries
print(type(check_if_exist))


print(str(check_if_exist) + '\n')

for country in countries:
    print(country)

del countries