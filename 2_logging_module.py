import logging
from abc import ABC, abstractmethod


logging.debug("DEBUG")  # NO OUTPUT
logging.info("INFO")  # NO OUTPUT
logging.warning("TEST WARNING")  # WARNING:root:TEST WARNING
logging.error("TEST ERROR")  # ERROR:root:TEST ERROR
logging.critical("TEST CRITICAL")  # CRITICAL:root:TEST CRITICAL

# root is the name of the default logger
# the default logger logs events marked as WARNING or more server. which means log events [WARNING, ERROR, CRITICAL]

# that why the output is :

# WARNING:root:TEST WARNING
# ERROR:root:TEST ERROR
# CRITICAL:root:TEST CRITICAL

# #######################################################################################


class Level(ABC):
    name = "Unknown"

    @abstractmethod
    def showlogs(self, msg):
        pass


class DEBUG(Level):
    name = "DEBUG"

    def showlogs(self, msg):
        logging.debug(f"{self.name}[{msg}]")


class INFO(Level):
    name = "INFO"

    def showlogs(self, msg):
        logging.info(f"{self.name}[{msg}]")


class WARNING(Level):
    name = "WARNING"

    def showlogs(self, msg):
        logging.warning(f"{self.name}[{msg}]")


class ERROR(Level):
    name = "ERROR"

    def showlogs(self, msg):
        logging.error(f"{self.name}[{msg}]")


class CRITICAL(Level):
    name = "CRITICAL"

    def showlogs(self, msg):
        logging.critical(f"{self.name}[{msg}]")


debug = DEBUG()
info = INFO()
warning = WARNING()
error = ERROR()
critical = CRITICAL()

logs = [warning, error, critical]

for log in logs:
    log.showlogs("test")

# output :

# WARNING:root:WARNING[test]
# ERROR:root:ERROR[test]
# CRITICAL:root:CRITICAL[test]

# #######################################################################################
