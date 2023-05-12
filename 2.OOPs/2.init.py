

class Computer:

    # this type of method is automatically called 
    # this method is called everytime for each object

    def __init__(self) :
        print('hiiii')

    @staticmethod
    def config():
        print('Hp', '16GB', 'i7', 454300)


comp1 = Computer()
comp2 = Computer()

# config method call on obj reference
comp1.config()
comp2.config()