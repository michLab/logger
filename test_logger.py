from logger import Logger
import logging

my_logger = Logger(logger_name=__name__, console_level=logging.INFO)
my_logger.info('This it test info message')