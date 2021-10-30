<<<<<<< HEAD
class BankAccount(object):
    
    def __init__(self, name, money, adress):
        self.name = name # global
        self.__money = money # private
        self.adress = adress
    
    # get and set global
    def getMoney(self):
        return self.__money
    
    def setMoney(self, amount):
        self.__money = amount
    
    # private
    def __increase(self):
        self.__money = self.__money + 500

p1 = BankAccount("messi", 1000, "barcelona")
p2 = BankAccount("neymar", 2000, "paris")

print("get method:",p1.getMoney())

p1.setMoney(5000)
print("after set method:",p1.getMoney())

# p1.__increase()
# print("after raise:",p1.getMoney())




=======
class BankAccount(object):
    
    def __init__(self, name, money, adress):
        self.name = name # global
        self.__money = money # private
        self.adress = adress
    
    # get and set global
    def getMoney(self):
        return self.__money
    
    def setMoney(self, amount):
        self.__money = amount
    
    # private
    def __increase(self):
        self.__money = self.__money + 500

p1 = BankAccount("messi", 1000, "barcelona")
p2 = BankAccount("neymar", 2000, "paris")

print("get method:",p1.getMoney())

p1.setMoney(5000)
print("after set method:",p1.getMoney())

# p1.__increase()
# print("after raise:",p1.getMoney())




>>>>>>> eb09223803fff446083f2dd7139f4cb94a088eff
