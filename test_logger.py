from logger import Logger
import logging

my_logger = Logger(logger_name=__name__, file_name="./test.log",
                   console_level=logging.INFO, file_level=logging.DEBUG)
message_number = 1
my_logger.info('This it a test info message with num %d', message_number)
my_logger.debug('This it a test debug message %s', str(message_number))
my_logger.warning('This it a test warning message')
my_logger.error('This it a test error message')
my_logger.critical('This it a test critical message')

a = 5
b = 0
try:
    c = a/b
except Exception as e:
    my_logger.exception("Exception occured")

