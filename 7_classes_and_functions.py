# - up until now we have been using the default logger [root].
# - the logging module contains several classes we can init to create our own logger.


# ############# ############# ############# ############# ############# ############


# Logger: used to represent our custom logger & using custom method to customize the logger.

# LogRecord: loggers automatically create LogRecord objs that have all info of the event being logged
# like: logger name, the function, the lineno and the message. [output of LogRecord that we will see]

# ############# ############# ############# ############# ############# ############

# (Handlers): represent output destinations
# Handlers: send the LogRecord to the required output destination, like a console or file.
# StreamHandler(Handler) for console, RotatingFileHandler(Handler) for log file.
# StreamHandler & RotatingFileHandler are subclasses[children] of (Handler) class.
# SMTPHandler: for email logging messages
# HttpHandler: for sending log messages to web server through GET/POST http methods


# Formatter: Used to specify the format of the output by a specifying a string format that lists out the attributes
# that the output should contain.

# ############# ############# ############# ############# ############# ############
import logging

# logger = logging.getLogger("example logger")
# logger.warning("this is warning.")  # this is warning. ==> logger obj has no default format, WE JUST SEE THE MESSAGE.
# logging.warning("this is warning")  # WARNING:root:this is warning ==> [level:log name:message]

# ############# ############# ############# ############# ############# ############

# attach 'handlers' to 'logger' that we can use it.

# __name__: special name variable that represents the current module name.

# ############# ############# ############# ############# ############# ############

# create new logger obj
logger = logging.getLogger(__name__)  # __name__ is value of %(name)s [logger name]
FORMAT = "[%(name)s] [%(asctime)s] [%(process)d] [%(levelname)s] [%(pathname)s:%(lineno)s] [%(message)s]"
DATETIME_FORMAT = "%d/%b/%Y %H:%M:%S"

logging.basicConfig(
    level=logging.DEBUG, format=FORMAT, datefmt=DATETIME_FORMAT,
)
logger.warning(
    "testing logger"
)  # ==>  __main__ - WARNING - testing logger ==> [name - level - msg]
logging.warning("testing with logging ")  # ==> root - WARNING - testing with logging.
# because we are not using custom [logger]
