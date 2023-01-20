from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk
import csv
import datetime
import logging
import os
import sys
import traceback
from pathlib import Path

sys.dont_write_bytecode = True

# Dir Path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
# IMPORT_PATH = None
# EXPORT_PATH = None

# IMPORT_PATH = os.path.join(ROOT_PATH, "Import")
# EXPORT_PATH = os.path.join(ROOT_PATH, "Export")

# file_in_path = "\\".join(
#     [IMPORT_PATH, "quarterly_sample_308_schedule_output.csv"])
# file_out_path = "\\".join([EXPORT_PATH, "sample_308_schedule_output.csv"])

# Logging Configuration
LOG_PATH = "\\".join([ROOT_PATH, "\\"])
LOG_FILE = (
    LOG_PATH + str(datetime.datetime.now().strftime("%m%d%Y")) +
    "_Q_Schedule_Importer_Logs.txt"
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

new_fileds = ["Sample ID", "Location", "Day",
              "Hour", "Hourly Swipe", "Bucket", "Sample Set"]
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
                SAMPLE_ID = row["sample_id"]
                LOCATION = row["loc"]
                DAY = row["day_type"]
                HOUR = row["begin_time"]
                HOURLY_SWIPE = row["swipes"]
                BUCKET = row["strata"]
                SAMPLE_SET = str(row["sample_id"])[1:4]

                new_rows.append(
                    {
                        "Sample ID": SAMPLE_ID,
                        "Location": LOCATION,
                        "Day": DAY,
                        "Hour": HOUR,
                        "Hourly Swipe": HOURLY_SWIPE,
                        "Bucket": BUCKET,
                        "Sample Set": SAMPLE_SET,
                    }
                )

    except FileNotFoundError as e:
        __isFailed = True
        print("\n\n[Error]:", e)
        op_text.insert('1.0', traceback.FrameSummary())
        print(traceback.FrameSummary())
        # logging.exception(e)
    except BaseException as e:
        print("\n\n[Error]:", e)
        op_text.insert('1.0', traceback.FrameSummary())
        print(traceback.FrameSummary())
        # logging.exception(e)
    else:
        print("\n\nFile Successfully Imported")
        op_text.insert('1.0', "File Successfully Imported")
        # logging.info("File Successfully Imported")


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
        logging.info(
            "File Successfully Exported!\n[File Path]: " + file_out_path)


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

def close():
    # win.destroy()
    app.quit()


def import_file():
    """
    Import CSV file to reproduce columns

    Args: param1: File import path

    Returns: Void
    """
    filetypes = (
        ('CSV files', '*.csv'),
        ('All files', '*.*')
    )
    # show the open file dialog
    impf = fd.askopenfile(
        filetypes=filetypes,
        initialdir=os.getcwd())

    # Import file in path
    IMPORT_FILE = impf.name

    # EXPORT_PATH = impf.__dir__
    # print("export_path0:", EXPORT_PATH)
    EXPORT_PATH = Path(impf.name)

    # EXPORT_PATH = EXPORT_PATH.parent + "\quarterly_sample_308_schedule_output.csv"

    print("1:", EXPORT_PATH.parent)
    print("2:", EXPORT_PATH.parent.as_posix())
    print("3:", EXPORT_PATH)

#     [IMPORT_PATH, "quarterly_sample_308_schedule_output.csv"])
    # print("export_path:", EXPORT_PATH)

    imp_txt.insert('1.0', IMPORT_FILE)
    exp_txt.insert('1.0', EXPORT_PATH.parent.as_posix())

    try:
        with open(IMPORT_FILE) as file:
            csv_file = csv.DictReader(file, delimiter=",")
            # Read CSV rows and generates new format to export
            for row in csv_file:
                SAMPLE_ID = row["sample_id"]
                LOCATION = row["loc"]
                DAY = row["day_type"]
                HOUR = row["begin_time"]
                HOURLY_SWIPE = row["swipes"]
                BUCKET = row["strata"]
                SAMPLE_SET = str(row["sample_id"])[1:4]

                new_rows.append(
                    {
                        "Sample ID": SAMPLE_ID,
                        "Location": LOCATION,
                        "Day": DAY,
                        "Hour": HOUR,
                        "Hourly Swipe": HOURLY_SWIPE,
                        "Bucket": BUCKET,
                        "Sample Set": SAMPLE_SET,
                    }
                )

    except FileNotFoundError as e:
        # __isFailed = True
        print("\n\n[Error]:", e)
        op_text.insert('1.0', e)
        # logging.exception(e)
    except BaseException as e:
        print("\n\n[Error]:", e)
        op_text.insert('1.0', e)
        # logging.exception(e)
    else:
        print("\n\nFile Successfully Imported")
        op_text.insert('1.0', "File Successfully Imported")
        # logging.info("File Successfully Imported")


def export_file():
    # show the open file dialog
    expf = fd.askdirectory(
        title="Export Directory"
        # initialdir = os.getcwd()
    )
    # read the csv file and show its name with path
    exp_txt.insert('1.0', expf)


# def output_result():
#     # op_result = "any exception"
#     # initialdir = os.getcwd()

#     # read the csv file and show its name with path
#     op_text.insert('1.0', opr_txt)


# App window
app = tk.Tk()
app.title('SFE Schedule Template Converter')
app.resizable(False, False)
app.geometry('658x350')

# Import Path
imp_txt = tk.Text(app, height=1, width=70, wrap=tk.NONE)
imp_txt.grid(row=0, column=1, columnspan=3)

tk.Label(app, text='Import Path').grid(row=0, column=0, pady=2)
tk.Label(app, text='Export Path').grid(row=1, column=0)

exp_txt = tk.Text(app, height=1, width=70, wrap=tk.NONE)
exp_txt.grid(row=1, column=1, columnspan=3)

# import file button
import_button = ttk.Button(
    app,
    text='Open a File',
    command=import_file
)

# export file button
export_button = ttk.Button(
    app,
    text='Set Export Folder',
    command=export_file
)

cnvrt_button = ttk.Button(
    app,
    text='Convert',
    # command=convert
)


exit_button = ttk.Button(app, text="Close", command=close)

import_button.grid(column=0, row=2, padx=3, pady=15)
export_button.grid(column=1, row=2, padx=3, pady=15, sticky="w")
exit_button.grid(column=2, row=2, padx=10, pady=15, sticky="e")

# print("opr_txt:", opr_txt)


op_text = tk.Text(app, height=15, wrap=tk.WORD)
op_text.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

app.mainloop()


# print(new_rows)
# [{'Sample ID': 'N308SAT1000000', 'Location': 'R507', 'Day': 'SAT', 'Hour': '12', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000001', 'Location': 'C11', 'Day': 'SAT', 'Hour': '13', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000002', 'Location': 'R130', 'Day': 'SAT', 'Hour': '10', 'Hourly Swipe': '32', 'Bucket': '1', 'Sample Set': '308'}]
