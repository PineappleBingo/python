import logging
from open_csv import CSV

# Logging Configuration
LogFile = r"D:\gitprojects\python\Modules\logging\main_log.txt"
LogFormat = "%(asctime)s  %(name)s:%(funcName)s [%(levelname)s] %(message)s"
LogDateFormat = "%m/%d/%Y %I:%M:%S %p"

logging.basicConfig(
    filename=LogFile, level=logging.DEBUG, format=LogFormat, datefmt=LogDateFormat
)

file_path = r"D:\gitprojects\python\Modules\logging\data1.csv"
CSV(file_path)

# Reference:
# https://docs.python.org/3/library/logging.html
# https://docs.python.org/3/howto/logging.html
