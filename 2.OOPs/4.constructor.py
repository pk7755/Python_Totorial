

class Computer:

    def __init__(self,brand,ram,cpu,price) :
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.price=price
    # for printing the object attribute values 
    def config(self):
        print('config is :', self.brand, self.ram, self.cpu, self.price )

    # update methods
    def updateBrand(self,brand):
        self.brand=brand
    def updateRam(self,ram):
        self.ram=ram
    def updateCpu(self,cpu):
        self.cpu=cpu
    def updatePrice(self,price):
        self.price=price


    
    # Method for comparing the two objects
    def compare(self,other):
        if self.brand==other.brand and self.ram == other.ram and self.cpu == other.cpu and self.price == other.price :
            return True
        else:
            return False


# Object creation
c1 = Computer('Hp', '16GB', 'i7', 454300)
c2 = Computer('Dell', '8GB', 'i5', 434300)
c3 = Computer('Dell', '8GB', 'i5', 434300)


c3.updateBrand('Acer')

# config method call on obj reference
c1.config()
c2.config()
c3.config()

if c3.compare(c2) :
    print("They are same .")
else:
    print("They are different.")
