# Python Logger Class
A class uses python logging module. 
It allows to simoltanously write log messages to log file and to the console.
The levels for the file and the console can be determined by contructor,
as well as the output file name. The constructor allows to change the default
formatter. In default formatter the time is unix time (seconds.microseconds).

## How to use

In this example a logger object is created:
```python
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
```

**Console:**
> 1569666439.207746 __main__     INFO       This it a test info message with num 1
> 
> 1569666439.226380 __main__     WARNING    This it a test warning message
> 
> 1569666439.226536 __main__     ERROR      This it a test error message
> 
> 1569666439.226661 __main__     CRITICAL   This it a test critical message
> 
> 1569666439.226796 __main__     ERROR      Exception occured
> 
> Traceback (most recent call last):
> 
>  File "test_logger.py", line 16, in <module>
> 
>     c = a/b
> 
> ZeroDivisionError: integer division or modulo by zero


**File:**
> 1569666439.207746 __main__     INFO       This it a test info message with num 1
> 
> 1569666439.226125 __main__     DEBUG      This it a test debug message 1
> 
> 1569666439.226380 __main__     WARNING    This it a test warning message
> 
> 1569666439.226536 __main__     ERROR      This it a test error message
> 
> 1569666439.226661 __main__     CRITICAL   This it a test critical message
> 
> 1569666439.226796 __main__     ERROR      Exception occured
>
> Traceback (most recent call last):
> 
>  File "test_logger.py", line 16, in <module>
> 
>     c = a/b
> 
> ZeroDivisionError: integer division or modulo by zero

## License
The contents of this repository are covered under the [MIT License](./LICENSE.txt)

