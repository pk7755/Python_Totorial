
class Student:


    def __init__(self, name, roll_no):
        self.name  = name
        self.roll_no  =roll_no
        self.Laptop=self.Laptop

    def show(self):
        print("Studentdetails : ", self.name, self.roll_no)

    
    class Laptop:

        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def show(self):
            print("Laptop details : ",self.brand, self.cpu, self.ram)


s1 = Student("Pradyumna",18786)
s2 = Student("shivam",18790)
lap1 = s1.Laptop("HP","i7",16)
lap2 = s2.Laptop("Dell","i7",16)
s1.show()
lap1.show()
s2.show()
lap2.show()







