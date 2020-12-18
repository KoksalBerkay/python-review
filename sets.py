empty_set = set()

countries= {'Belgium', 'Germany', 'France', 'Netherland', 'Poland'}
print(countries)

birthyears= {1985,1986,1988,1989,1999}
print(birthyears)

# We can have different types of data inside Sets.
that_man = {42, 'smart', 1.70, True, ('tennis', 'walking')}
print(that_man)

# Unlike tuple we can add and remove an item to/from a Set. But we can not change the item itself.
birthyears.add(2000)
print(birthyears)

birthyears.remove(1986)
print(birthyears),

# update() method can be used to add multiple items at once.
birthyears.update([2001,2002,2003,2004])
print(birthyears)

# You can iterate through each item in a Set using for loop
for i in birthyears:
    print(i)

# clear() method makes empty set.
birthyears.clear()
print(birthyears)
