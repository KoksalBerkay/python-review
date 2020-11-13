magicians = ['alice', 'david', 'carolina']

# for <variable> in <range/collection>:
    #do something

for magician in magicians:
    print(magician)

# print(magician) # if you use print() out of the for loop it prints latest assignment


###### Actualy what for has done for us ######
# magician = magicians[0]
# print(magician)
# magician = magicians[1]
# print(magician)
# magician = magicians[2]
# print(magician)


# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

for magician in magicians:
    print(type(magician))

for magician in magicians:
    print(magician.title() + "  that was great show \nI look forward to seeing your next show with \n")

print("Thanks everyone, it was great show")