#  HOMEWORK 04

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

#   •	 Print the message, The first three items in the list are: Then use a slice to
#           print the first three items from that program’s list

#   •	 Print the message, Three items from the middle of the list are: Use a slice
#           to print three items from the middle of the list

#   •	 Print the message, The last three items in the list are: Use a slice to print
#           the last three items in the list


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60) Make a copy of the list of pizzas, and call it friend_pizzas
# Then, do the following:

#   •	 Add a new pizza to the original list

#   •	 Add a different pizza to the list friend_pizzas

#   •	 Prove that you have two separate lists Print the message, My favorite
#           pizzas are:, and then use a for loop to print the first list Print the message,
#           My friend’s favorite pizzas are:, and then use a for loop to print the second list
#           Make sure each new pizza is stored in the appropriate list


# 4-10
pizza_list = ["margarita", "pepperoni", "cheddar", "bumbum", "tatuş", "kaşarlı", "vegan"]

first_three = pizza_list[0:3]
print ("The first three items in the list are: ")
print (first_three)

middle_three = pizza_list[2:5]
print ("Three items from the middle of list are: ")
print (middle_three)

last_three = pizza_list[-3:]
print ("The last three items are in the list are: ")
print (last_three)


# 4-11
friend_pizzas = pizza_list
pizza_list.append("senin kafan")
friend_pizzas.append("ayak")

for pizza in friend_pizzas:
    print(pizza)


for other_pizza in pizza_list:
    print(other_pizza)