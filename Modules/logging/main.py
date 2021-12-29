import csv
import logging
import open_csv

LogFile = r"D:\gitprojects\python\Modules\logging\main_log.txt"
logging.basicConfig(filename='LogFile', level=logging.DEBUG)


def CSV(file_path):

    try:
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                STO_LOC1 = row[1]

        print(STO_LOC1)

    # If file not found
    except FileNotFoundError:
        print("File not found")
    # If any other exception occured, it would move file
    except Exception as e:
        print("Not Processed: ", file_path, "\n", e)
        # error = True
