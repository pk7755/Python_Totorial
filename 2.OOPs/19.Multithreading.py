from threading import *

class A(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
class B(Thread):
    def run(self):
        for i in range(10):
            print("hii")
class C(Thread):
    def run(self):
        for i in range(10):
            print("hlw")


r1 = A()
r2 = B()
r3 = C()

r1.start()
r2.start()
r3.start()


