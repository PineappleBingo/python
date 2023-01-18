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

file_in_path = "\\".join([IMPORT_PATH, "Sample.csv"])
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

# Variables
__isFailed = None

new_fileds = ["Sample Id", "Counts", "Control Area"]
new_rows = []


def IMPORT_CSV(file_in_path):
    """
    Import CSV file to reproduce columns

    Args: param1: File import path

    Returns: Void
    """

    global __isFailed
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
    except BaseException as e:
        print("\n\n[Error]:", e)
        logging.exception(e)
    else:
        print("\n\nFile Successfully Imported")
        logging.info("File Successfully Imported")


def EXPORT_CSV(file_out_path):
    """
    Export modified rows to CSV file

    Aarg: param1: file destination path

    Returns: Void
    """
    try:
        with open(file_out_path, "w", encoding="UTF8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=new_fileds)
            writer.writeheader()
            writer.writerows(new_rows)

    except BaseException as e:
        print("\n\nNot Processed: ", file_out_path, "[Error]:", e)
        logging.exception(e)
    else:
        print("File Successfully Exported!\n[File Path]: " + file_out_path)
        logging.info("File Successfully Exported!\n[File Path]: " + file_out_path)


# try:
#     IMPORT_CSV(file_in_path)
#     if __isFailed:
#         input("\n\nPress Enter to Quit...")
#     else:
#         EXPORT_CSV(file_out_path)
#         input("\n\nPress Enter to Quit...")

# except Exception as e:
#     print("[Error]:", e)
#     input("\n\nPress Enter to Quit...")


from tkinter import *

app = Tk()

Label(app, text='Import Path').grid(row=0)
Label(app, text='Export Path').grid(row=1)
IFP = Entry(app, width=70)
EFP = Entry(app, width=70)

IFP.grid(row=0, column=1)
EFP.grid(row=1, column=1)

IFP_Btn = Button(app, text="Open")
EFP_Btn = Button(app, text="Open")

IFP_Btn.grid(row=0, column=2)
EFP_Btn.grid(row=1, column=2)

ourMessage ='This is our Message'
messageVar = Message(app, text = ourMessage)

messageVar.config(bg='lightgreen')
messageVar.grid(row=2)

mainloop()

# https://realpython.com/python-gui-tkinter/


# print(new_rows)
# [{'Sample Id': 'N3080000001', 'Counts': '10', 'Control Area': '308'},
#  {'Sample Id': 'N3070000002', 'Counts': '20', 'Control Area': '307'},
#  {'Sample Id': 'Q1350000003', 'Counts': '30', 'Control Area': '135'},
#  {'Sample Id': 'Q1500000004', 'Counts': '40', 'Control Area': '150'}]
