from tkinter import filedialog as fd
import tkinter.scrolledtext as tkscrolled
from tkinter import ttk
import tkinter as tk
import csv
import datetime
import os
import sys
import traceback
from pathlib import Path

sys.dont_write_bytecode = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
IMPORT_PATH = None
EXPORT_PATH = None


new_fileds = ["Sample ID", "Location", "Day",
              "Hour", "Hourly Swipe", "Bucket", "Sample Set"]
new_rows = []


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


def import_file():
    """
    Import CSV file
    """
    global EXPORT_PATH
    global IMPORT_PATH

    implog_tx = str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p "))

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
        print("\n[Error]:", e)
        op_text.insert('1.0', e)
    except BaseException as e:
        print("\n[Error]:", e)
        op_text.insert('1.0', e)
    else:
        print("\n" + implog_tx + impf_name + " Successfully Imported")
        op_text.insert('1.0', implog_tx + impf_name + " Successfully Imported")
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


def convert_file():
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
                writer = csv.DictWriter(f, fieldnames=new_fileds)
                writer.writeheader()
                writer.writerows(new_rows)

        except BaseException as e:
            print("\nNot Processed: ", file_out_path, "[Error]:", e)
            op_text.insert(tk.END, "\n" + e)

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
import_button = ttk.Button(
    frame_BI,
    text='Open a File',
    command=import_file
)
# Export path setup button
export_button = ttk.Button(
    frame_BI,
    text='Set Export Path',
    command=set_export_path
)
# Convert execution button
cnvrt_button = ttk.Button(
    frame_BI,
    text='Convert',
    command=convert_file
)

exit_button = ttk.Button(frame_BI, text="Close", command=close)

frame_BI.grid_columnconfigure(0, weight=1)
frame_BI.grid_columnconfigure(1, weight=1)
frame_BI.grid_columnconfigure(2, weight=1)
frame_BI.grid_columnconfigure(3, weight=13)

import_button.grid(row=0, column=0, padx=3, pady=15, ipadx=10, sticky="w")
export_button.grid(row=0, column=1, padx=3, pady=15, ipadx=10, sticky="w")
cnvrt_button.grid(row=0, column=2, padx=3, pady=15, ipadx=20, sticky="w")
exit_button.grid(row=0, column=3, padx=10, pady=15, ipadx=10, sticky="e")

op_text = tkscrolled.ScrolledText(frame_CI, width=90, height=15, wrap=tk.WORD)
op_text.grid(row=0, column=0, padx=5, pady=5)

app.mainloop()


# print(new_rows)
# [{'Sample ID': 'N308SAT1000000', 'Location': 'R507', 'Day': 'SAT', 'Hour': '12', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000001', 'Location': 'C11', 'Day': 'SAT', 'Hour': '13', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000002', 'Location': 'R130', 'Day': 'SAT', 'Hour': '10', 'Hourly Swipe': '32', 'Bucket': '1', 'Sample Set': '308'}]
