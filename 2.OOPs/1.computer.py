

class Computer:
    @staticmethod
    def config():
        print('Hp', '16GB', 'i7', 454300)


comp1 = Computer()
comp2 = Computer()

# config method call on class reference
Computer.config()
Computer.config()


# config method call on obj reference
comp1.config()
comp2.config()