
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()

    def show(self):
        print("Student details : ", self.name, self.roll_no)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 16

        def show(self):
            print("Laptop details : ", self.brand, self.cpu, self.ram)


s1 = Student("Pradyumna", 18786)
s2 = Student("Shivam", 18790)

lap1 = Student.Laptop()
lap2 = Student.Laptop()
s1.show()

s2.show()
