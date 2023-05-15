class A:
    def __init__(self):
        pass

    def demo(self):
        print("this is my demo method of  class A")

class B(A):
    def __init__(self):
        pass
    def demo(self):
        print("this is my demo method of class B")


a = B()
a.demo()

