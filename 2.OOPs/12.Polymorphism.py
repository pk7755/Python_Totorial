class Pycharm:

    def execute(self):
        print("Pycharm ide")

class VSCode:

    def execute(self):
        print("VS code ide")

class Laptop:

    def code(self,ide):
        ide.execute()

# ide = Pycharm()
ide = VSCode()
lap1 = Laptop()
lap1.code(ide)
