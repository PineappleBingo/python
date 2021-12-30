import logging
from open_csv import CSV

LogFile = r"D:\gitprojects\python\Modules\logging\main_log.txt"
logging.basicConfig(filename="LogFile", level=logging.DEBUG)

file_path = r"D:\gitprojects\python\Modules\logging\data.csv"

CSV(file_path)
