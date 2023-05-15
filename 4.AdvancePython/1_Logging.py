from logging import *

""" 
Python logging is a module that allows you to track events that occur while your program is running.
And logging is a useful tool for debugging, troubleshooting, and monitoring your program.

There are three steps to configuring Python logging:

1.Choose a logger - This is where the object that will actually do the logging.
2.Configure the logger - This step involves telling the logger to log messages, what format to use, and what level of detail to include.
3.Use the logger - This step simply involves using the logger object in your code to log messages

Python Logging Level

Python logging levels are used to indicate the severity of a message. 
There are five logging levels in Python: 

1.  DEBUG       --> 10
2.  INFO        --> 20
3.  WARINING    --> 30
4.  ERROR       --> 40
5.  CRITICAL    --> 50

NOTE : WARNING is a default stage, meaning only messages with a group of WARNING or higher will be logged. 

"""
debug("this is debug")
info("This is info")
warning("This is warning.")
error("This is eror.")
critical("This is critical.")