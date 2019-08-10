import logging
import sys
import time

class Logger:
    def __init__(self, logger_name='__name__', file_name='app.log',
                 file_level=logging.DEBUG, console_level=logging.INFO,
                 formatter='%(created).6f %(name)-12s %(levelname)-8s %(message)s'):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        
        self.console_formatter = logging.Formatter(formatter)
        self.console_level = console_level
        self.init_console_handler()
        self.logger.addHandler(self.console_handler)

        self.file_name = file_name
        self.file_level = file_level
        self.file_formatter = logging.Formatter(formatter)
        self.init_file_handler()
        self.logger.addHandler(self.file_handler)

        self.logger.propagate = False
            

    def init_console_handler(self):
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setFormatter(self.console_formatter)
        self.console_handler.setLevel(self.console_level)
    

    def init_file_handler(self):
        self.file_handler = logging.FileHandler(self.file_name)
        self.file_handler.setFormatter(self.file_formatter)
        self.file_handler.setLevel(self.file_level)


    def debug(self, msg):
        self.logger.debug(msg)


    def info(self, msg):
        self.logger.info(msg)
    

    def warning(self, msg):
        self.logger.warning(msg)
        

    def error(self, msg):
        self.logger.error(msg)


    def critical(self, msg):
        self.logger.critical(msg)




