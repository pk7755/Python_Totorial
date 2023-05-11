

class Computer:

    # this type of method is automatically called 
    # this method is called everytime for each object

    def __init__(self,brand,ram,cpu,price) :
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.price=price

    def config(self):
        print('config is :', self.brand, self.ram, self.cpu, self.price )


comp1 = Computer('Hp', '16GB', 'i7', 454300)
comp2 = Computer('Dell', '8GB', 'i5', 434300)

# config method call on obj reference
comp1.config()
comp2.config()