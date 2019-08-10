# Python Logger Class
A class uses python logging module. 
It allows to simoltanously write log messages to log file and to the console.
The levels for the file and the console can be determined by contructor,
as well as the output file name. The constructor allows to change the default
formatter. In default formatter the time is unix time (seconds.microseconds).

## How to use

In this example a logger object is created, where:
* `my_cute.log` is the name of the output file
* `logging.DEBUG` is the level set to the file output
* `logging.INFO` is the level set to the console output

```python
logger = Logger(__name__, 'my_cute.log', logging.DEBUG, logging.INFO)
logger.debug('A debug message')
logger.info('An info message')
logger.warning('A warning message')
logger.error('An error message')
logger.critical('A critical message')
```

**Console:**
> 1565436200.911726 __main__     INFO     An info message
> 1565436200.913647 __main__     WARNING  A warning message
> 1565436200.914586 __main__     ERROR    An error message
> 1565436200.915454 __main__     CRITICAL A critical message

**File:**
> 1565436200.898947 __main__     DEBUG    A debug message
> 1565436200.911726 __main__     INFO     An info message
> 1565436200.913647 __main__     WARNING  A warning message
> 1565436200.914586 __main__     ERROR    An error message
> 1565436200.915454 __main__     CRITICAL A critical message

## License
The contents of this repository are covered under the [MIT License](./LICENSE.txt)

