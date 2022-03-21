from multi_logger_confi import proc_logger
from multi_logger_confi import errs_logger
from open_csv import CSV

file_path = r"D:\gitprojects\python\Modules\logging\data1.csv"

proc_logger.info("Run Main Process")
proc_logger.info("Run CSV()")

CSV(file_path)

proc_logger.info("Complete Task")


# Reference:
# https://gist.github.com/muya/2dff1cd8c5b42f1dabab