import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler("Emplog1.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# get path using os.path & get current directory.
logger.addHandler(ch)
logger.addHandler(fh)

class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
        logger.info(f'{self.empid}, {self.name}, {self.salary}, {self.email}')
    
    def empInfo(self):
        print(self.empid,self.name,self.salary)

    @property
    def email(self):
        return '{}.@gmail.com'.format(self.name)
    


e1 = Employee(101, 'Scott', 3000)
e2 = Employee(102, 'Fredy', 4000)
e3 = Employee(103, 'Sohan', 3500)
e4 = Employee(104, 'MOhan', 3300)
