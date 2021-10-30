<<<<<<< HEAD
class Animal: # parent

    def toString(self):
        print("animal")

class Monkey(Animal):
    
    def toString(self):
        print("monkey")

a1 = Animal()
a1.toString()

m1 = Monkey()
=======
class Animal: # parent

    def toString(self):
        print("animal")

class Monkey(Animal):
    
    def toString(self):
        print("monkey")

a1 = Animal()
a1.toString()

m1 = Monkey()
>>>>>>> eb09223803fff446083f2dd7139f4cb94a088eff
m1.toString() # monkey calls overriding method