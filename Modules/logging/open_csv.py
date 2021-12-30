import csv
import logging


def CSV(file_path):
    logger = logging.getLogger("open_csv:CSV")
    try:
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                TP = row["TimePeriod"]

                print(TP)

    # If file not found
    except FileNotFoundError as e:
        print("[Error]:", e)
        logger.exception(e)
    # If any other exception occured, it would move file
    except Exception as e:
        print("Not Processed: ", file_path, "[Error]:", e)
        logger.exception(e)
        # error = True