from logging import *


'''
filename: This parameter is used to specify the filename that the logging messages will be written to.

filemode: This parameter is used to specify the mode that the file will be opened. The default mode is 'a', which means that messages 
will be appended to the end of the file.

Format: This parameter is used to specify the format of the logging messages. The default format is '%(levelname)s: %(message)s', which means that the level name and message will be printed.

datefmt: This parameter is used to specify the date format of the logging messages. 

Level: This parameter is used to specify the minimum level of messages that will be logged. The default level is 'WARNING', which means that only messages with a level of 'WARNING' or higher will be logged.

'''
LOG_FORMAT='{lineno} -- {name} -- {message} -- {asctime} '
basicConfig(filename='Logfile.log', level=DEBUG, filemode='w', format=LOG_FORMAT, style='{')

debug("this is debug.")
info("This is info.")
warning("This is warning.")
error("This is eror.")
critical("This is critical.")