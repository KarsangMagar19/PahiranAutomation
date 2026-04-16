import logging
import os

def get_logger(name="framework"):
    if not os.path.exists("reports/logs"):
        os.makedirs("reports/logs")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("reports/logs/test.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger