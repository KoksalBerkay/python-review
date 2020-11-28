# LIST COMPHERENSION

cubes = [number**3 for number in range(1,10)]

print(cubes)


# SLICING
stones = ['bishop', 'queen', 'king', 'knight', 'private', 'horse']

#whole list
whole = stones[:]


#first three
first_three = stones[0:3]

# is step possible? Yes possible 
guess= stones[0:6:2] # [::2]


# the last two
last_two = stones[-2:]

#looping in slice

for stone in stones[3:]:
    print(stone)
    
new_list = stones[3:]
for stone in new_list:
    print(stone)

pizza_list = ["margarita" , "pepperoni" , "cheddar", "bumbum", "ayak"]

# the first method:
new_list_01 = pizza_list.copy()

# the second method:
new_list_02 = pizza_list[:]

# the third method:
new_list_03 = list(pizza_list)

# the fourth method (cloning):
new_list_04 = pizza_list
