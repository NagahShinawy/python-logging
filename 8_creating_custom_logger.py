import logging
DATETIME_FORMAT = "%d/%b/%Y %H:%M:%S"

C_FORMAT = "[%(name)s] [%(asctime)s] [%(process)d] [%(levelname)s] [%(pathname)s:%(lineno)s] [%(message)s]"


logger = logging.getLogger(__name__)

# todo: 1- create CONSOLE handler
chandler = logging.StreamHandler()

# todo: 2- set severity level for CONSOLE handler
chandler.setLevel(
    logging.WARNING
)  # use levels [WARNING, ERROR, CRITICAL] for chandler [console]

# todo: 3- setup and attaching logging format for CONSOLE handler
c_format = logging.Formatter(C_FORMAT)
chandler.setFormatter(c_format)

# todo: 4- link CONSOLE handler to logger obj
logger.addHandler(chandler)
# ############# # ############## ############## ############## ############## ############## #############

F_FORMAT = "[%(name)s] [%(asctime)s] [%(levelname)s] [%(message)s]"

# todo: 1- create file handler
fhandler = logging.FileHandler("file.log")

# todo: 2- set severity level for FILE handler
fhandler.setLevel(
    logging.ERROR
)  # use levels [ERROR, CRITICAL] for fhandler [file handler]

# todo: 3- setup and attaching logging format for FILE handler
f_format = logging.Formatter(F_FORMAT)
fhandler.setFormatter(f_format)

# todo: 4- link FILE handler to logger obj
logger.addHandler(fhandler)

# ########### ########### ########### ########### ########### ########### ########### ########### ##########

# todo: actually log your events
# given severity levels are (WARNING, ERROR, CRITICAL for chandler) and (ERROR, CRITICAL] for fhandler )
logger.info("testing info")  # no output because your using 'info' that less that given severity levels


# no output for logfile.log [fhandler because severity level for fhandler at least ERROR]
# so, it accepts ERROR, CRITICAL.
logger.warning("testing warning")  # output just for console severity levels WARNING, ERROR, CRITICAL.


logger.error("testing errors")  # output for both console(chandler) & logfile(fhandler). it matches severity levels
