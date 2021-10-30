<<<<<<< HEAD
# parent
class Animal():
    
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal walk")


# child
class Monkey(Animal):
    def __init__(self):
        super().__init__() # use init of parent
        print("monkey is created")
        
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")
class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
        
    def fly(self):
        print("fly")
#
m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()
print("-----")
b1 = Bird()
b1.walk()
b1.fly()






=======
# parent
class Animal():
    
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal walk")


# child
class Monkey(Animal):
    def __init__(self):
        super().__init__() # use init of parent
        print("monkey is created")
        
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")
class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
        
    def fly(self):
        print("fly")
#
m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()
print("-----")
b1 = Bird()
b1.walk()
b1.fly()






>>>>>>> eb09223803fff446083f2dd7139f4cb94a088eff
