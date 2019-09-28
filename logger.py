"""logger.py: The Logger class definition file"""

__author__ = "Michal Labowski"
__version__ = "0.1.0.2"
__mantainer__ = "Michal Labowski"
__status__ = "Prototype"

import sys
import time
import logging

class Logger:
    """A Logger class definition - it allows to simultanously write data to log file
    and the console"""

    def __init__(self, logger_name='__name__', file_name=' ',
                 file_level=-1, console_level=-1,
                 formatter='%(created).6f %(name)-12s %(levelname)-10s %(message)s'):
        """
        Initializes the Logger class instance

        :param logger_name: str name of the logger
        :param file_name: str name of the log file
        :param file_level: the severity level of messages output to log file
        :param console_level: the severity level of messages output to console
        :param formatter: the format of the log message
        """
        self.logger = logging.getLogger(logger_name)
        # The severity level of the root logger
        # All events equal and above this level will be logged
        self.logger.setLevel(logging.DEBUG)  
        self.initialized = False
        
        if console_level in {logging.DEBUG, logging.INFO, logging.WARNING,
                logging.ERROR, logging.CRITICAL}:
            # Initialize the console output only when needed:
            self.console_formatter = logging.Formatter(formatter)
            self.console_level = console_level
            self.init_console_handler()
            self.logger.addHandler(self.console_handler)
            self.initialized = True

        if (file_name is not ' ') and (file_level in {logging.DEBUG,
                logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL}):
            # Initialize the file output only when nedded:
            self.file_name = file_name
            self.file_level = file_level
            self.file_formatter = logging.Formatter(formatter)
            self.init_file_handler()
            self.logger.addHandler(self.file_handler)
            self.initialized = True

        self.logger.propagate = False

    def init_console_handler(self):
        """ Initialize the console output"""
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setFormatter(self.console_formatter)
        self.console_handler.setLevel(self.console_level)
    
    def init_file_handler(self):
        """Initialize the file output"""
        self.file_handler = logging.FileHandler(self.file_name)
        self.file_handler.setFormatter(self.file_formatter)
        self.file_handler.setLevel(self.file_level)

    def debug(self, msg, *args, **kwargs):
        """Set debug message"""
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """Set info message"""
        self.logger.info(msg, *args, **kwargs)
    
    def warning(self, msg, *args, **kwargs):
        """Set warning message"""
        self.logger.warning(msg, *args, **kwargs)
        
    def error(self, msg, *args, **kwargs):
        """Set error message"""
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """Set critical message"""
        self.logger.critical(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        """Set exception message"""
        self.logger.exception(msg, *args, **kwargs)
