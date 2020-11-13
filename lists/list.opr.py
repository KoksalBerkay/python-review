motorbikes = ["honda", "yamaha", "suzuki"]
print(motorbikes)
# changing an Element by index
motorbikes[1] = "ducati"
print(motorbikes)
# Adding an element to a list using append method
motorbikes.append("yamaha")
print(motorbikes)
# adding element to particular posititon using insert method
motorbikes.insert(0,"java")
print(motorbikes)
# Removing item using del keyword
del motorbikes[0]
print(motorbikes)
# remove item using pop method
motorbikes.insert(0,"java") # java inserted again
print(motorbikes)
# pop() method default removes last item
removed_item = motorbikes.pop()
print(removed_item)
print(motorbikes)
dublicated_list = ["yamaha", "yamaha", "yamaha"]
# we can define which item to be poped.
removed_item = motorbikes.pop(0)
print(removed_item)
print(motorbikes)
# Empty lists
my_empty_list = []
my_empty_list.append("Paris")
