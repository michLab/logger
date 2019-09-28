import threading
from time import sleep
import logger

my_logger = logger.Logger(logger_name=__name__, file_name="./test.log",
                          console_level=logger.INFO, file_level=logger.DEBUG)
message_number = 1
my_logger.info('This is a test info message with num %d', message_number)
my_logger.debug('This is a test debug message %s', str(message_number))
my_logger.warning('This is a test warning message')
my_logger.error('This is a test error message')
my_logger.critical('This is a test critical message')

a = 5
b = 0
try:
    c = a/b
except Exception as e:
    my_logger.exception("Exception occured")

logger_with_thread = logger.Logger(logger_name=__name__, file_name="./test_thread.log",
                          console_level=logger.INFO, file_level=logger.DEBUG)

def producer_callback(name="Default producer", arg_logger=None):
    logger = arg_logger
    while True:
        if logger:
            logger.info('[%s]: This is a test info message', name)
            sleep(0.001)
        else:
            return 

producer_A = threading.Thread(target=producer_callback, kwargs=dict(arg_logger=logger_with_thread,
                                                                    name="Producer A"))
producer_A.daemon=True
producer_A.start()

producer_B = threading.Thread(target=producer_callback, kwargs=dict(arg_logger=logger_with_thread,
                                                                    name="Producer B"))
producer_B.daemon=True
producer_B.start()

while True:
    print("Still running...")
    sleep(10)
