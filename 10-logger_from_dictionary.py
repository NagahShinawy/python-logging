import logging
import logging.config
import yaml

# with open("config.yaml", "r") as yamlf:
#     config = yaml.safe_load(yamlf.read())
#     logging.config.dictConfig(config)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} in {pathname}-{funcName}-{lineno}: {message}",
            "style": "{",
            "datefmt": "[%d/%b/%Y %H:%M:%S]",
        },
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}


logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

logger.info("testing info")