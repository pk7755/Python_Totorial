class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B:
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")


a1 = A()
# with the help of a1 , we can only access the methods of class A
a1.feature1()
a1.feature2()

b1 = B()
# with the help of b1 , we can only access the methods of class B
b1.feature3()
b1.feature4()

# than inheritence comes under picture
# if we want to access all the method of class A  and class B in class C


# Multiple inheritance allowed in python 
class C(A, B):
    def feature5(self):
        print("feature 5 is working")


c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
