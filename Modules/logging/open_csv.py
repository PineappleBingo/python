import csv
import logging


def CSV(file_path):
    logger = logging.getLogger("open_csv")
    try:
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                TP = row["TimePeriod"]

                print(TP)

    # If file not found
    except FileNotFoundError as e:
        print("[Error Mssg]:", e)
        logging.error(e, exc_info=True)  # same as logger.exception(e)
        logger.error("Fatal error in main loop", exc_info=True)
        logger.warn("Cannot resolve conflicting : {}".format(e))
        logger.error("Not Processed / {}".format(e), exc_info=True)
    # If any other exception occured, it would move file
    except Exception as e:
        print("Not Processed: ", file_path, "[Error]:", e)

        logging.error(e, exc_info=True)  # same as logger.exception(e)
        logger.error("Fatal error in main loop", exc_info=True)
        logger.warn("Cannot resolve conflicting : {}".format(e))
        logger.error("Not Processed / {}".format(e), exc_info=True)
