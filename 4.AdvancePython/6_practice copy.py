import logging
import os

logger = logging.getLogger('pk')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('{lineno} -- {asctime} -- {message}',style='{')
file_handler = logging.FileHandler(f'{os.getcwd()}\pradyu.log.log')
logger.addHandler(file_handler)
file_handler.setFormatter(formatter)
# LOG_FORMAT = '{lineno} -- {asctime} -- {message}'
# logging.basicConfig(filename='logsfile.log',filemode='w',style='{',format=LOG_FORMAT,level=logging.DEBUG)


def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    return a / b


num_1 = 10
num_2 = 20
add_result = add(num_1, num_2)
logging.debug('Add : {} + {} = {} '.format(num_1,num_2,add_result))


sub_result = subtract(num_1, num_2)
logging.debug('Sub : {} - {} = {} '.format(num_1,num_2,sub_result))


mul_result = mul(num_1, num_2)
logging.debug('Mul : {} * {} = {} '.format(num_1,num_2,mul_result))


div_result = div(num_1, num_2)
logging.debug('Div : {} / {} = {} '.format(num_1,num_2,div_result))


