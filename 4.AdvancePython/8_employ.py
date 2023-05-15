import logging

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# get path using os.path & get current directory.
file_handler = logging.FileHandler('C:/Users/pradkumar/Documents/Python/EmpLog1.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:

    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
     
        logging.warning(f'{self.empid} , {self.name}, {self.salary}, {self.email}')
    
    def empInfo(self):
        print(self.empid,self.name,self.salary)
    @property
    def email(self):
        return '{}.@gmail.com'.format(self.name)
    


e1 = Employee(101, 'Scott', 3000)
e2 = Employee(102, 'Scott', 3000)
e3 = Employee(103, 'Scott', 3000)
e4 = Employee(104, 'Scott', 3000)