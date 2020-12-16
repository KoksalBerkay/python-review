empty_dic = {}

integer_dic = {1: 'Belgium', 2: 'Germany', 3:'Netherland', 4:'France'}
print(integer_dic)

mixed_dic = {1: 'Automation', 'program': 'Python', 'numbers':[1,2,3]}

###### selecting stuff from a dictionary ######
that_man = {'name': 'KodMan', 'birth': 1978, 'hobbies': ['tennis', 'ski']}
print(that_man['name'])
print(that_man['hobbies'])
print(that_man['hobbies'][0])

###### update that_man name ######
that_man['name'] = 'CodeMan'
print(that_man)

###### adding 'lastname' into that_man ######
that_man['lastname'] = 'Byte'
print(that_man)

###### We are using pop() method to remove an item from a dictionary ######
that_man.pop('lastname')
print(that_man)

###### looping in a dictionary #####
for i in that_man:
    print('that man:', i)

###### if you use iterated keys inside square brackets the whole will be printed ######
for i in that_man:
    print('that man:', that_man[i])

# You may want to delete your all key/value pairs in the dictionary. In this case you can use clear() method
###### that_man.clear()

# This method will not delete a dictionary but makes it empty. To delete entire object use del command.
###### del that_man