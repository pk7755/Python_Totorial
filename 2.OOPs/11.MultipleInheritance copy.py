class A:
    def __init__(self):
        print("in init of A")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B():
    def __init__(self):
        print("in init of B")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("in init of C")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")


# In the case of multiple inheritance the super()._init() is call  the left most class of init()
# In python we have a concept of MRO --> Method Resolution Order ,  because of that we can use multiple inheritance in python 
# C(A, B)----- class A will be prefered 
# C(B, A)----- class B will be prefered 
a1 = C()
