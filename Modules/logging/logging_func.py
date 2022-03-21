import datetime
import logging
from logging import FileHandler
from logging import Formatter

formatter = logging.Formatter( '%(asctime)s - [%(name)s]:%(levelname)-8s %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p" )

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
