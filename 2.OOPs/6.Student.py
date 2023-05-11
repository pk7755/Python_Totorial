
class Student:

    school="Jspider"

    def __init__(self, m1, m2, m3):
        self.m1  = m1
        self.m2  = m2
        self.m3  = m3

    def avg(self):
        print("Average is :",(self.m1 + self.m2 + self.m3)/3)
    
    def stdprint(self):
        print("Student marks details : ", self.m1, self.m2, self.m3)
    
    # if you want to use that method at class level
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is a student class in ......abc module...................")


s1 = Student(23, 34, 23)
s2 = Student(34, 56, 23)
s3 = Student(45, 38, 37)

s1.stdprint()
s1.avg()
s2.stdprint()
s2.avg()
s3.stdprint()
s3.avg()
print(s3.getSchool())
print(Student.getSchool())


Student.info()
s1.info()




