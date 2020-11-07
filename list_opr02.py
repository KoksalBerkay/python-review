cars = ["honda", "ferrari", "mini", "lamborgini", "mercedes", "bmw", "toyota"]
cars_sorted = cars

#Sort alphabetical A-Z /// Warning this is permanent
cars_sorted.sort()
print(cars)
print(cars_sorted)
# Sort alphabetical Z-A
cars.sort(reverse=True)

# how can I preserve original order in my "cars" list?
print("/n")

cars_new = ["honda", "ferrari", "mini", "lamborgini", "mercedes", "bmw", "toyota"]
print(cars_new)
cars_sorted_new = sorted(cars_new)

print(cars_sorted_new)

#Reverse the whole list // it is only reverse not alphabetical.
cars_sorted_new.reverse()
cars_new.reverse()

print(cars_sorted_new)
cars_sorted_new.reverse()

my_number = [5,100,25,14,9,1.7]
my_number_sorted = sorted(my_number)
# my_number.sort()

# Fining the Length of a list
carsLength = len(cars)