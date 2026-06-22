import logging

logger = logging.getLogger(__name__)
logger.info("Opening Home Page")

#logger.debug("Technical details")
logger.info("Normal execution")
logger.warning("Something unexpected")
logger.error("Step failed")
#logger.critical("Framework crash")

import logging

def get_logger():
    logger = logging.getLogger()

    if not logger.hasHandlers():
        logging.basicConfig(
            filename="automation.log",#dictates where logs are saved
            level=logging.INFO, #DEBUG/ERROR/WARNING/CRITICAL
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    return logger