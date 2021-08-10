import logging
from abc import ABC, abstractmethod


# info func calls basicConfig internally, so the default config will be used at the all of program
# because basicConfig can only be called once.

# todo: comment & uncomment this line for better understanding.
# todo: make sure basicConfig is called before we start logging any events.

logging.info("info BEFORE basicConfig with default logger")

logging.basicConfig(
            level=logging.DEBUG,
            # filename="app.log",
            format="%(name)s - %(levelname)s - %(message)s",
        )

logging.info("info AFTER basicConfig with our new logger config")
# basicConfig can only be called once.

# the severity level functions [debug, info, warning, error, critical] call basicConfig internally
# if it has not been called before.

# that means we must call basicConfig() ourselves before we use any of the severity level functions.[ 5 funcs]

# calling basicConfig() by ourselves just like override the default configurations
# [default logger name is root, default level is: WARNING].

# after first time one of [severity function] is called, you can no longer called basicConfig
# on the default logger, because those functions[ 5 funcs] already called basicConfig


class BasicLevel(ABC):
    name = "Unknown"

    @abstractmethod
    def showlogs(self, msg):
        pass


class DebugLevel(BasicLevel):
    name = "DEBUG"

    def showlogs(self, msg):
        logging.debug(f"{self.name}[{msg}]")


class InfoLevel(BasicLevel):
    name = "INFO"

    def showlogs(self, msg):
        logging.info(f"{self.name}[{msg}]")


class WarningLevel(BasicLevel):
    name = "WARNING"

    def showlogs(self, msg):
        logging.warning(f"{self.name}[{msg}]")


class ErrorLevel(BasicLevel):
    name = "ERROR"

    def showlogs(self, msg):
        logging.error(f"{self.name}[{msg}]")


class CriticalLevel(BasicLevel):
    name = "CRITICAL"

    def showlogs(self, msg):
        logging.critical(f"{self.name}[{msg}]")


debug = DebugLevel()
info = InfoLevel()
warning = WarningLevel()
error = ErrorLevel()
critical = CriticalLevel()

logs = [debug, info, warning, error, critical]

for log in logs:
    log.showlogs("test")

# output is :


# DEBUG:root:DEBUG[test]
# INFO:root:INFO[test]
# WARNING:root:WARNING[test]
# ERROR:root:ERROR[test]
# CRITICAL:root:CRITICAL[test]

# because __init__ of [BasicLevel] using least severe [logging.DEBUG],
# so DEBUG event or more severe. means all levels will be logged
# because you are using DEBUG[ the least severe.
# debug or greater are logged
