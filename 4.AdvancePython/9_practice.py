import logging
class LoggerDemo:
    def sample_logger(self):
        #Create logger
        logger = logging.getLogger("DemoLog")
        logger.setLevel(logging.DEBUG)
        #create console handler or file handler and set the log level
        ch = logging.StreamHandler()
        fh = logging.FileHandler("demologfile.log")
        #create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s ',datefmt='%m/%d/%Y %I:%M:%S %p')
        
        # add formatter to console or file handler
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        #application code - log message
        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")

ld = LoggerDemo()
ld.sample_logger()


     