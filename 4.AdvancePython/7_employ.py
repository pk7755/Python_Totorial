import logging
import os

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=f'{os.getcwd()}\EmpLog.log', filemode='a',format=LOG_FORMAT, level=logging.INFO)
 
class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
     
        logging.info('{} , {}, {}, {}'.format(self.empid,self.name,self.salary,self.email))
    
    def empInfo(self):
        print(self.empid,self.name,self.salary)
    @property
    def email(self):
        return'{}.@gmail.com'.format(self.name)

e1 = Employee(101, 'Scott', 3000)
e2 = Employee(102, 'Fredy', 4000)
e3 = Employee(103, 'Sohan', 3500)
e4 = Employee(104, 'MOhan', 3300)
