import csv
import datetime
import logging
import os
import sys

sys.dont_write_bytecode = True

# Dir Path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
IMPORT_PATH = os.path.join(ROOT_PATH, "Import")
EXPORT_PATH = os.path.join(ROOT_PATH, "Export")

file_in_path = "\\".join([IMPORT_PATH, "Sample1.csv"])
file_out_path = "\\".join([EXPORT_PATH, "Output.csv"])

# Logging Configuration
LOG_PATH = "\\".join([ROOT_PATH, "\\"])
LOG_FILE = (
    LOG_PATH + str(datetime.datetime.now().strftime("%m%d%Y")) + "_Q_Schedule_Logs.txt"
)
LogFormat = "%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s"
LogDateFormat = "%m/%d/%Y %I:%M:%S %p"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    filemode="w",
    format=LogFormat,
    datefmt=LogDateFormat,
)

__isFailed = False

new_fileds = ["Sample Id", "Counts", "Control Area"]
new_rows = []


def IMPORT_CSV(file_in_path):
    global __isFailed
    __isFailed = False
    try:
        with open(file_in_path) as file:
            csv_file = csv.DictReader(file, delimiter=",")
            # Read CSV rows and generates new format to export
            for row in csv_file:
                SAMPLE_ID = row["Sample ID"]
                COUNTS = row["Counts"]
                CONTR_AREA = str(row["Sample ID"])[1:4]

                new_rows.append(
                    {
                        "Sample Id": SAMPLE_ID,
                        "Counts": COUNTS,
                        "Control Area": CONTR_AREA,
                    }
                )

    except FileNotFoundError as e:
        __isFailed = True
        print("\n\n[Error]:", e)
        logging.exception(e)
        # input("\n\nPress Enter to Quit...")
    # except BaseException as e:
    #     print("Not Processed: ", file_in_path, "[Error]:", e)
    #     logging.exception(e)
    #     input("\n\nPress Enter to Quit...")
    else:
        print("\n\nFile Successfully Imported")
        logging.info("File Successfully Imported")


def EXPORT_CSV(file_out_path):
    try:
        with open(file_out_path, "w", encoding="UTF8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=new_fileds)
            writer.writeheader()
            writer.writerows(new_rows)

    except BaseException as e:
        print("\n\nNot Processed: ", file_out_path, "[Error]:", e)
        logging.exception(e)
    else:
        print("\n\nFile Successfully Exported!\n[File Path]: " + file_out_path)
        logging.info("File Successfully Exported!\n[File Path]: " + file_out_path)


try:
    IMPORT_CSV(file_in_path)
    print(__isFailed)
    if __isFailed:
        # print(__isFailed)
        # raise Exception
        input("\n\nPress Enter to Quit...")
    else:
        EXPORT_CSV(file_out_path)

except Exception as e:
    print("[Error]:", e)
    input("\n\nPress Enter to Quit...")

# finally:
#     input("\n\nPress Enter to Quit...")

# print(new_rows)
# [{'Sample Id': 'N3080000001', 'Counts': '10', 'Control Area': '308'},
#  {'Sample Id': 'N3070000002', 'Counts': '20', 'Control Area': '307'},
#  {'Sample Id': 'Q1350000003', 'Counts': '30', 'Control Area': '135'},
#  {'Sample Id': 'Q1500000004', 'Counts': '40', 'Control Area': '150'}]
