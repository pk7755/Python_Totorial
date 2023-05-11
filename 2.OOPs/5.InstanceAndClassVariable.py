class car :
    type = 'Petrol' # -------------------> class variable
    def __init__(self,brand,price): #----> instance variable
        self.brand=brand
        self.price = price

    def printCar(self):
        print("Car details is :",self.brand, self.price, self.type)


c1 = car('BMW',345343234)
c2 = car('Maruti',4534332)


car.type = "Electric car" #--------------- update on class reference
c2.price = 343434343      #--------------- update on object reference

c1.printCar()
c2.printCar()

