########### EXERCİSE 01-10 ###########
#Ex01
# name = "Köksal Berkay Denktaş"
# adress = "Turkey \n İzmir \n Basınsitesi \n 172/2 Street \n No: 2"
# print("Name: " + name + "\nAdress: " + adress)

#Ex02
# users_name = input("Enter your name")
# print("Hello " + users_name)

#Ex03
# widht = float(input("Give your room's widht in meter"))
# length = float(input("Give your room's lenght in meter"))
# area = widht * length
# area = ("%.3f" % area) #here we are limiting decimal points to two numbers
# print("The area is", area, "square meters")

#Ex05
# less_than_a_liter_containers = int(input("Enter the number of less than a liter containers "))
# much_than_a_liter_containers = int(input("Enter the number of much than a liter containers "))
# deposit_for_less_than = 0.10
# deposit_for_much_than = 0.25
# fee1 = deposit_for_less_than * less_than_a_liter_containers
# fee2 = deposit_for_much_than * much_than_a_liter_containers
# total_fee = fee1 + fee2
# total_fee = ("%.2f" % total_fee)
# print("Your deposit is: $", total_fee)

#Ex07
# n = int(input("Please give a positive number"))
# sum_n = n * (n + 1) / 2
# print(int(sum_n))

#Ex08
# widget_weight = 75
# gizmo_weight = 112

# widget_amount = int(input("How many widget do you want to buy?"))
# gizmo_amount = int(input("How many widget do you want to buy?"))

# total_widget_weight = widget_amount * widget_weight
# total_gizmo_weight = gizmo_amount * gizmo_weight

# total_weight = total_widget_weight + total_gizmo_weight

# print("Total wigh is:",total_weight,"grams")

#Ex09
amount_of_money_1 = float(input("How many euros do you want to add your account"))
interest_per_year = 4 / 100

one_years_after = amount_of_money_1 * interest_per_year
amount_of_money_2 = amount_of_money_1 + one_years_after
amount_of_money_2 = float("%.2f" % amount_of_money_2)
print("Your new balance after one year is:",amount_of_money_2,"euros")

two_years_after = amount_of_money_2 * interest_per_year
amount_of_money_3 = amount_of_money_2 + two_years_after
amount_of_money_3 = float("%.2f" % amount_of_money_3)
print("Your new balance after two year is:",amount_of_money_3,"euros")

three_years_after = amount_of_money_3 * interest_per_year
amount_of_money_4  = amount_of_money_3 + three_years_after
amount_of_money_4 = float("%.2f" % amount_of_money_4)
print("Your new balance after three year is:",amount_of_money_4,"euros")




