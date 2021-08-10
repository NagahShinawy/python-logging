# saving config for use later on, or share with someone else. [config file]

# ######### ######### ######### ######### ######### ######### ########
# - we can configure the logger using a config file or dictionary.
# - this is useful for saving your config or modifying them in a running app.
# - fileConfig() , dictConfig()

import logging
import logging.config as conf

conf.fileConfig("file.conf", disable_existing_loggers=False)  # NOT disable other used loggers if they exist

logger = logging.getLogger(__name__)
logger.info("testing info level")