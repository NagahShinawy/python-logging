import logging
from logging import handlers

# 1- setup logging config
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# built in logging variables [ asctime, levelname, pathname, lineno, message, ....].
# asctime: time of creation of log record.
# logging variables: are part of log record
# logging record: is meta data that is associated with certain event.
# example: [10/Aug/2021 11:31:30] INFO [E:/containers/learn-projects/python-logging/4_formatting_the_output.py:26] test


# 1-1 : adding log format
# datefmt="%d/%b/%Y %H:%M:%S" is easy to read more that default one and customizable, so we can change it on need.
format_ = logging.Formatter(
    "[%(asctime)s] [%(process)d] [%(levelname)s] [%(pathname)s:%(lineno)s] [%(message)s]",
    datefmt="%d/%b/%Y %H:%M:%S",
)


# 2- for console logging [console handle ch]
ch = logging.StreamHandler()
ch.setFormatter(format_)
logger.addHandler(ch)

# 3- for file logging [file handler fh]
fh = handlers.RotatingFileHandler("logs.log", maxBytes=(1048576 * 5), backupCount=7)
fh.setFormatter(format_)
logger.addHandler(fh)

logger.info("testing")
logger.warning("testing waring")
logger.error("testing error")
logger.critical("testing critical")
logger.debug("testing DEBUG")