from tkinter import filedialog as fd
import tkinter.scrolledtext as tkscrolled
from tkinter import ttk
import tkinter as tk
import csv
import datetime
import os
import pandas as pd
import sys
import traceback
from pathlib import Path

sys.dont_write_bytecode = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
IMPORT_PATH = None
EXPORT_PATH = None
CSV_PATH = None


qs_fileds = ["Sample ID", "Location", "Day",
             "Hour", "Hourly Swipe", "Bucket", "Sample Set"]
qs_new_rows = []

ws_fileds = ["SSC Date", "SSC Start", "SSC End", "Checker", "Bus", "Job Number", "Job Code", "Job Name",
             "Description", "Start Time", "End Time", "Depot", "Location", "Destination", "Rel Trip", "Checker Name"]
ws_new_rows = []


def close():
    """
    Close the application
    """
    app.quit()


def reset():
    """
    Reset the application
    """
    imp_txt.delete('1.0', tk.END)
    exp_txt.delete('1.0', tk.END)
    op_text.delete('1.0', tk.END)


def error_msg():
    """Display Exception in a messagebox"""
    errlog_ts = str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p "))
    err_message = traceback.format_exc()

    print("\n[Error]: An uncaught exception has occurred")
    print("\n", err_message)
    print("\n" + errlog_ts + " application terminating... ")
    op_text.insert('1.0', "[Error]: An uncaught exception has occurred")
    op_text.insert(tk.END, "\n\n" + err_message)
    op_text.insert(tk.END, "\n" + errlog_ts + " Application terminating... ")


def import_qs_file():
    """
    Import Quarterly Schedule CSV file
    """
    global EXPORT_PATH
    global IMPORT_PATH

    implog_ts = str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p "))

    filetypes = (
        ('CSV files', '*.csv'),
        ('All files', '*.*')
    )
    # show the open file dialog
    impf = fd.askopenfile(
        filetypes=filetypes,
        initialdir=ROOT_PATH)

    # Import file in path
    IMPORT_PATH = impf.name
    # Import file name
    impf_name = Path(impf.name).name

    # Pass if export path already set up by user
    if EXPORT_PATH:
        pass
    else:
        # Set Default export file path same as import file location
        EXPORT_PATH = Path(impf.name).parent.as_posix()

    reset()

    imp_txt.insert('1.0', IMPORT_PATH)
    exp_txt.insert('1.0', EXPORT_PATH)

    try:
        with open(IMPORT_PATH) as file:
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

                qs_new_rows.append(
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

    except FileNotFoundError:
        error_msg()
    except BaseException:
        error_msg()
    else:
        print("\n" + implog_ts + impf_name + " Successfully Imported")
        op_text.insert('1.0', implog_ts + impf_name + " Successfully Imported")
        # op_text.insert('1.0', "File Successfully Imported")


def set_export_path():
    """
    Set export path other than default path
    Default export path is set to import path

    """
    global EXPORT_PATH
    # show the open file dialog
    expf = fd.askdirectory(
        title="Export Directory"
        # initialdir = os.getcwd()
    )
    # read the csv file and show its name with path
    exp_txt.delete('1.0', tk.END)
    EXPORT_PATH = expf
    exp_txt.insert('1.0', EXPORT_PATH)


def convert_qs_file():
    """
    Export modified rows to CSV file
    """

    if IMPORT_PATH and EXPORT_PATH:

        expf_ts = str(datetime.datetime.now().strftime("%m%d%Y_%I%M%S"))
        explog_ts = str(datetime.datetime.now().strftime(
            "%m/%d/%Y %I:%M:%S %p "))

        file_out_path = "/".join([str(EXPORT_PATH),
                                 ("sample_308_schedule_output_" + expf_ts + ".csv")])

        try:
            with open(file_out_path, "w", encoding="UTF8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=qs_fileds)
                writer.writeheader()
                writer.writerows(qs_new_rows)

        except BaseException:
            error_msg()

        else:
            print(
                explog_ts + "File Successfully Converted & Exported!\n[File Path]: " + file_out_path)
            op_text.insert(tk.END, "\n" + explog_ts +
                           "File Successfully Converted & Exported!")
            op_text.insert(tk.END, "\n[File Path]: " + file_out_path)
            op_text.insert(
                tk.END, "\n---------------------------------------------------------------------------------")

    elif IMPORT_PATH and EXPORT_PATH is None:
        op_text.insert(tk.END, "\nPlease Select Export File Location")
        print("Please Select Export File Location")
    elif EXPORT_PATH and IMPORT_PATH is None:
        op_text.insert(tk.END, "\nPlease Select Import File(.csv)")
        print("Please Select Import File")
    else:
        op_text.insert(
            tk.END, "\nPlease Select Import File & Export File Location")
        print("Please Select Import File & Export File Location")


def excel_to_csv(file_path):
    """
    Convert Excel file to CSV & .xlsx to .csv
    """
    global CSV_PATH

    try:
        # Convert .xlsx extion to .csv
        CSV_PATH = Path(file_path).with_suffix(".csv").as_posix()
        # convert excel extension to csv
        excel_file = pd.read_excel(file_path)
        excel_file.to_csv(CSV_PATH, index=None, header=True)

    except FileNotFoundError:
        error_msg()
    except BaseException:
        error_msg()


def import_ws_file():
    """
    Import Weekly Schedule CSV file
    """
    global EXPORT_PATH
    global IMPORT_PATH

    implog_ts = str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p "))

    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )
    # show the open file dialog
    impf = fd.askopenfile(
        filetypes=filetypes,
        initialdir=ROOT_PATH)

    # Import file in path
    IMPORT_PATH = impf.name
    # Import file name
    impf_name = Path(impf.name).name

    # Convert excel file to csv
    excel_to_csv(IMPORT_PATH)
    print("CSV_PATH:", CSV_PATH)

    # Pass if export path already set up by user
    if EXPORT_PATH:
        pass
    else:
        # Set Default export file path same as import file location
        EXPORT_PATH = Path(impf.name).parent.as_posix()

    reset()

    imp_txt.insert('1.0', IMPORT_PATH)
    exp_txt.insert('1.0', EXPORT_PATH)

    try:
        with open(CSV_PATH) as file:
            csv_file = csv.DictReader(file, delimiter=",")
            # Read CSV rows and generates new format to export
            for row in csv_file:
                SSC_DATE = row["SSC_DATE"]
                SSC_START = row["ASM_START_TIME"]
                SSC_END = row["ASM_END_TIME"]
                CHECKER = row["SSC_CHECKER"]
                BUS = row["BUS_PES"]
                JOB_NO = row["PES_JOB_NO"]
                JOB_CODE = row["PES_JOB_CODE"]
                JOB_NAME = row["PES_JOB_NAME"]
                DISCRIPTION = row["PES_DESCRIPTION"]
                START_TIME = row["PES_START_TIME"]
                END_TIME = row["PES_END_TIME"]
                DEPOT = row["PES_DEPOT"]
                LOCATION = row["PES_LOCATION"]
                DESTINATION = row["PES_DESTINATION"]
                REL_TRIP = row["PES_REL_TRIP"]
                CHECKER_NAME = row["CHECKER_NAME"]
                # BUCKET = row["Tablet"]

                ws_new_rows.append(
                    {
                        "SSC Date": SSC_DATE,
                        "SSC Start": SSC_START,
                        "SSC End": SSC_END,
                        "Checker": CHECKER,
                        "Bus": BUS,
                        "Job Number": JOB_NO,
                        "Job Code": JOB_CODE,
                        "Job Name": JOB_NAME,
                        "Description": DISCRIPTION,
                        "Start Time": START_TIME,
                        "End Time": END_TIME,
                        "Depot": DEPOT,
                        "Location": LOCATION,
                        "Destination": DESTINATION,
                        "Rel Trip": REL_TRIP,
                        "Checker Name": CHECKER_NAME,
                    }
                )

    except FileNotFoundError:
        error_msg()
    except BaseException:
        error_msg()
    else:
        print("\n" + implog_ts + impf_name + " Successfully Imported")
        op_text.insert('1.0', implog_ts + impf_name + " Successfully Imported")
        # op_text.insert('1.0', "File Successfully Imported")


def convert_ws_file():
    """
    Export modified rows to CSV file
    """

    if IMPORT_PATH and EXPORT_PATH:

        expf_ts = str(datetime.datetime.now().strftime("%m%d%Y_%I%M%S"))
        explog_ts = str(datetime.datetime.now().strftime(
            "%m/%d/%Y %I:%M:%S %p "))

        file_out_path = "/".join([str(EXPORT_PATH),
                                 ("Weekly_sample_308_schedule_output_" + expf_ts + ".csv")])

        try:
            with open(file_out_path, "w", encoding="UTF8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=ws_fileds)
                writer.writeheader()
                writer.writerows(ws_new_rows)

        except BaseException:
            error_msg()

        else:
            print(
                explog_ts + "File Successfully Converted & Exported!\n[File Path]: " + file_out_path)
            op_text.insert(tk.END, "\n" + explog_ts +
                           "File Successfully Converted & Exported!")
            op_text.insert(tk.END, "\n[File Path]: " + file_out_path)
            op_text.insert(
                tk.END, "\n---------------------------------------------------------------------------------")

    elif IMPORT_PATH and EXPORT_PATH is None:
        op_text.insert(tk.END, "\nPlease Select Export File Location")
        print("Please Select Export File Location")
    elif EXPORT_PATH and IMPORT_PATH is None:
        op_text.insert(tk.END, "\nPlease Select Import File(.xlsx)")
        print("Please Select Import File")
    else:
        op_text.insert(
            tk.END, "\nPlease Select Import File & Export File Location")
        print("Please Select Import File & Export File Location")


# App window
app = tk.Tk()
app.title('SFE Schedule Template Converter')
app.resizable(False, False)
appWindow_w = 750
appWindow_h = 400
app.geometry("{}x{}".format(appWindow_w, appWindow_h))

# Frame Geometry
frame_A = tk.Frame(app, width=appWindow_w, height=100)
frame_AI = tk.Frame(frame_A, width=appWindow_w)
frame_A.grid(row=0, column=0)
frame_AI.pack(side=tk.LEFT, padx=5, pady=8, expand=1)

frame_B = tk.Frame(app, width=appWindow_w, height=60)
frame_BI = tk.Frame(frame_B, width=appWindow_w)
frame_B.grid(row=1, column=0)
frame_BI.place(x=0, y=5, width=appWindow_w-10, height=50)
# frame_BI.pack(side=tk.LEFT, pady=5, padx=5, expand=1, fill=tk.X)

frame_C = tk.Frame(app, width=appWindow_w, height=200)
frame_CI = tk.Frame(frame_C, width=appWindow_w)
frame_C.grid(row=2, column=0)
frame_CI.pack(side=tk.LEFT, padx=5, pady=5, expand=1)

frame_AI.grid_columnconfigure(0, weight=1)
frame_AI.grid_columnconfigure(1, weight=1)

# Import Path
tk.Label(frame_AI, text='Import Path', width=10).grid(
    row=0, column=0, sticky="w")
imp_txt = tk.Text(frame_AI, width=80, height=1, wrap=tk.NONE)
imp_txt.grid(row=0, column=1, sticky="e")

tk.Label(frame_AI, text='Export Path', width=10).grid(
    row=1, column=0, sticky="w")
exp_txt = tk.Text(frame_AI, width=80, height=1, wrap=tk.NONE)
exp_txt.grid(row=1, column=1, sticky="e")

# Import file open button
import_qs_button = ttk.Button(
    frame_BI,
    text='Quarterly Schedule',
    command=import_qs_file
)
# Export path setup button
export_button = ttk.Button(
    frame_BI,
    text='Set Export Path',
    command=set_export_path
)
# Convert execution button
cnvrt_qs_button = ttk.Button(
    frame_BI,
    text='QS Convert',
    command=convert_qs_file
)
# Import file open button
import_ws_button = ttk.Button(
    frame_BI,
    text='Weekly Schedule',
    command=import_ws_file
)
# Convert execution button
cnvrt_ws_button = ttk.Button(
    frame_BI,
    text='WS Convert',
    command=convert_ws_file
)

exit_button = ttk.Button(frame_BI, text="Close", command=close)

frame_BI.grid_columnconfigure(0, weight=1)
frame_BI.grid_columnconfigure(1, weight=1)
frame_BI.grid_columnconfigure(2, weight=1)
frame_BI.grid_columnconfigure(3, weight=1)
frame_BI.grid_columnconfigure(4, weight=1)
frame_BI.grid_columnconfigure(5, weight=10)

import_qs_button.grid(row=0, column=0, padx=3, pady=15, ipadx=10, sticky="w")
export_button.grid(row=0, column=1, padx=3, pady=15, ipadx=10, sticky="w")
cnvrt_qs_button.grid(row=0, column=2, padx=3, pady=15, ipadx=20, sticky="w")
import_ws_button.grid(row=0, column=3, padx=3, pady=15, ipadx=10, sticky="w")
cnvrt_ws_button.grid(row=0, column=4, padx=3, pady=15, ipadx=20, sticky="w")
exit_button.grid(row=0, column=5, padx=10, pady=15, ipadx=10, sticky="e")

op_text = tkscrolled.ScrolledText(frame_CI, width=90, height=15, wrap=tk.WORD)
op_text.grid(row=0, column=0, padx=5, pady=5)

app.mainloop()


# print(new_rows)
# [{'Sample ID': 'N308SAT1000000', 'Location': 'R507', 'Day': 'SAT', 'Hour': '12', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000001', 'Location': 'C11', 'Day': 'SAT', 'Hour': '13', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000002', 'Location': 'R130', 'Day': 'SAT', 'Hour': '10', 'Hourly Swipe': '32', 'Bucket': '1', 'Sample Set': '308'}]
