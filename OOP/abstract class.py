<<<<<<< HEAD
from abc import ABC, abstractmethod

class Animal(ABC): # super class

    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass

class Bird(Animal): # sub class
    
    def __init__(self):
        print("bird")
    
    def walk(self):
        print("walk")
    
    def run(self):
        print("run")
        
b1 = Bird()









=======
from abc import ABC, abstractmethod

class Animal(ABC): # super class

    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass

class Bird(Animal): # sub class
    
    def __init__(self):
        print("bird")
    
    def walk(self):
        print("walk")
    
    def run(self):
        print("run")
        
b1 = Bird()









>>>>>>> eb09223803fff446083f2dd7139f4cb94a088eff
