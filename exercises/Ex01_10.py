########### EXERCİSE 01-10 ###########
#Ex01
name = "Köksal Berkay Denktaş"
adress = "Turkey \n İzmir \n Basınsitesi \n 172/2 Street \n No: 2"
print("Name: " + name + "\nAdress: " + adress)

#Ex02
users_name = input("Enter your name")
print("Hello " + users_name)

#Ex03
widht = float(input("Give your room's widht in meter"))
length = float(input("Give your room's lenght in meter"))
area = widht * length
area = ("%.3f" % area) #here we are limiting decimal points to two numbers
print("The area is", area, "square meters")

#Ex05
less_than_a_liter_containers = int(input("Enter the number of less than a liter containers "))
much_than_a_liter_containers = int(input("Enter the number of much than a liter containers "))
deposit_for_less_than = 0.10
deposit_for_much_than = 0.25
fee1 = deposit_for_less_than * less_than_a_liter_containers
fee2 = deposit_for_much_than * much_than_a_liter_containers
total_fee = fee1 + fee2
total_fee = ("%.2f" % total_fee)
print("Your deposit is: $", total_fee)




