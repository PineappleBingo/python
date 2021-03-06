import datetime
import logging
from logging import FileHandler
from logging import Formatter

# opt.1
Proc_LogFormat = logging.Formatter(
    "%(asctime)s [%(module)13s][%(levelname)s] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)
Errs_LogFormat = logging.Formatter(
    "%(asctime)s [%(filename)s -> %(funcName)s():%(lineno)s] [%(levelname)s] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

# opt.2
# LogFormat = "%(asctime)s  %(name)s:%(funcName)s [%(levelname)s] %(message)s"
# LogFormat1 = "%(asctime)s [%(filename)s -> %(funcName)s():%(lineno)s] [%(levelname)s]:%(message)s"
# LogFormat2 = "%(asctime)s [%(filename)s:%(lineno)s - %(funcName)15s() ] %(message)s"

LOG_LEVEL = logging.INFO

# Process Logger
PROC_LOG_FILE = (
    "D:\\gitprojects\\python\\Modules\\logging\\"
    + str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    + "_Proc_log.txt"
)
proc_logger = logging.getLogger("System_Proc")
proc_logger.setLevel(LOG_LEVEL)
proc_logger_file_handler = FileHandler(PROC_LOG_FILE)
proc_logger_file_handler.setLevel(LOG_LEVEL)
# opt.1
proc_logger_file_handler.setFormatter(Proc_LogFormat)
# opt.2
# proc_logger_file_handler.setFormatter(LogFormat1)
proc_logger.addHandler(proc_logger_file_handler)

# Error Logger
ERRS_LOG_FILE = (
    "D:\\gitprojects\\python\\Modules\\logging\\"
    + str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    + "_Error_log.txt"
)
errs_logger = logging.getLogger("System_Errs")
errs_logger.setLevel(LOG_LEVEL)
errs_logger_file_handler = FileHandler(ERRS_LOG_FILE)
errs_logger_file_handler.setLevel(LOG_LEVEL)
# opt.1
errs_logger_file_handler.setFormatter(Errs_LogFormat)
# opt.2
# errs_logger_file_handler.setFormatter(LogFormat2)
errs_logger.addHandler(errs_logger_file_handler)
