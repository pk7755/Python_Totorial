from logging import *

LOG_FORMAT='{lineno} -- {asctime} --{name} -- {message} '

basicConfig(
            filename='Logfile.log', 
            level=DEBUG, filemode='w',
            format=LOG_FORMAT, 
            style='{', 
            datefmt='%d-%m-%Y %H:%M:%S'
            )

logger = getLogger('Pradyumna')

logger.debug("this is debug.")
logger.info("This is info.")
logger.warning("This is warning.")
logger.error("This is eror.")
logger.critical("This is critical.")