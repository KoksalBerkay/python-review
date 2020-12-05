# Below pizzas are sold in the pizza restaurant
pizzas = ['margaritha', 'pepperoni', 'salami',
          'beefking', 'meatball', 'mozarella']

# my favorite pizzas
my_favorites = ['potatomi', 'kaasprince',
                'margaritha', 'beefking', 'mozarella']


# Write a program check all available pizzas in store
# And then compare favorite pizzas.
# if it matches, add to my_cart list object
# At the end of the program print my_cart list.

# Hints:
# Use for
# use if

######### ANSWER #########

my_cart = []

for my_favorite in my_favorites:
    for pizza in pizzas:
        if pizza == my_favorite:
            my_cart.append(pizza)

print(my_cart)
