from abc import ABC, abstractmethod 

class computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(computer):
    def process(self):
        print("this is process method of laptop class")



com = Laptop()
com.process()
