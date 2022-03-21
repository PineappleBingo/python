import csv
from multi_logger_confi import proc_logger
from multi_logger_confi import errs_logger


def CSV(file_path):
    proc_logger.info("Open File(s):", file_path)
    try:
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                TP = row["TimePeriod"]

                print(TP)

    # If file not found
    except FileNotFoundError as e:
        print("[Error Mssg]:", e)
        errs_logger.error(e, exc_info=True)  # same as logger.exception(e)
        errs_logger.error("Fatal error in main loop", exc_info=True)
        errs_logger.warn("Cannot resolve conflicting : {}".format(e))
        errs_logger.error("Not Processed / {}".format(e), exc_info=True)
    # If any other exception occured, it would move file
    except Exception as e:
        print("Not Processed: ", file_path, "[Error]:", e)

        errs_logger.error(e, exc_info=True)  # same as logger.exception(e)
        errs_logger.error("Fatal error in main loop", exc_info=True)
        errs_logger.warn("Cannot resolve conflicting : {}".format(e))
        errs_logger.error("Not Processed / {}".format(e), exc_info=True)
