class A:
    def __init__(self):
        print("in init of A")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):
    def __init__(self):
        # we want to call the init() of parent class than we use super() 
        super().__init__()
        print("in init of B")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

# -------------- in the case of default constructor OR having their own constructor ----------------------------------
# if we are creating the object with the help of class A construstor than it will call the init method of class A
# if we are creating the object with the help of class B construstor than it will call the init method of class B

# --------------- if only Class A have it's own init() ----------------------------
# we are creating object with the help of class B constructor than it will call the init() of class A
# if class B is not having their own init()


a1 = B()
