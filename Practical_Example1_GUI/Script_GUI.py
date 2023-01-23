from tkinter import filedialog as fd
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
EXPORT_PATH = None

new_fileds = ["Sample ID", "Location", "Day",
              "Hour", "Hourly Swipe", "Bucket", "Sample Set"]
new_rows = []

def close():
    app.quit()

def import_file():
    """
    Import CSV file

    """
    global EXPORT_PATH

    filetypes = (
        ('CSV files', '*.csv'),
        ('All files', '*.*')
    )
    # show the open file dialog
    impf = fd.askopenfile(
        filetypes=filetypes,
        initialdir=ROOT_PATH)

    # Import file in path
    IMPORT_FILE = impf.name
    # Import file name
    impf_name = Path(impf.name).name
    # Set Default export file path same as import file path
    EXPORT_PATH = Path(impf.name).parent.as_posix()
    
    imp_txt.delete('1.0', tk.END)
    exp_txt.delete('1.0', tk.END)
    op_text.delete('1.0', tk.END)

    imp_txt.insert('1.0', IMPORT_FILE)
    exp_txt.insert('1.0', EXPORT_PATH)

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
        print("\n[Error]:", e)
        op_text.insert('1.0', e)
    except BaseException as e:
        print("\n[Error]:", e)
        op_text.insert('1.0', e)
    else:
        print("\n" + impf_name + " Successfully Imported")
        # op_text.insert('1.0', impf_name + "File Successfully Imported")
        op_text.insert('1.0', "File Successfully Imported")



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
    if EXPORT_PATH :
        
        ts = str(datetime.datetime.now().strftime("%m%d%Y_%I%M%S"))
        file_out_path = "/".join([str(EXPORT_PATH), ("sample_308_schedule_output_" + ts +".csv")])
        
        try:
            with open(file_out_path, "w", encoding="UTF8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=new_fileds)
                writer.writeheader()
                writer.writerows(new_rows)

        except BaseException as e:
            print("\nNot Processed: ", file_out_path, "[Error]:", e)
            op_text.insert(tk.END, "\n" + e)      
            # logging.exception(e)
        else:
            print("File Successfully Converted & Exported!\n[File Path]: " + file_out_path)
            op_text.insert(tk.END, "\nFile Successfully Converted & Exported!\n[File Path]: " + file_out_path)
            # logging.info(
            #     "File Successfully Exported!\n[File Path]: " + file_out_path)

    else:
        op_text.insert(tk.END, "\nPlease select export file location")
        print("Please select export file location")
    

# App window
app = tk.Tk()
app.title('SFE Schedule Template Converter')
app.resizable(False, False)
app.geometry('658x350')

# Import Path
imp_txt = tk.Text(app, height=1, width=70, wrap=tk.NONE)
imp_txt.grid(row=0, column=1, columnspan=4)

tk.Label(app, text='Import Path').grid(row=0, column=0, pady=2)
tk.Label(app, text='Export Path').grid(row=1, column=0)

exp_txt = tk.Text(app, height=1, width=70, wrap=tk.NONE)
exp_txt.grid(row=1, column=1, columnspan=4)

# import file button
import_button = ttk.Button(
    app,
    text='Open a File',
    command=import_file
)
# export file button
export_button = ttk.Button(
    app,
    text='Set Export Path',
    command=set_export_path
)

cnvrt_button = ttk.Button(
    app,
    text='Convert',
    command=convert_file
)

exit_button = ttk.Button(app, text="Close", command=close)

import_button.grid(column=0, row=2, padx=3, pady=15)
export_button.grid(column=1, row=2, padx=3, pady=15)
cnvrt_button.grid(column=2, row=2, padx=3, pady=15, sticky="w")
exit_button.grid(column=3, row=2, padx=10, pady=15, sticky="e")

op_text = tk.Text(app, height=15, wrap=tk.WORD)
op_text.grid(row=3, column=0, columnspan=4, padx=5, pady=10)

app.mainloop()


# print(new_rows)
# [{'Sample ID': 'N308SAT1000000', 'Location': 'R507', 'Day': 'SAT', 'Hour': '12', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000001', 'Location': 'C11', 'Day': 'SAT', 'Hour': '13', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000002', 'Location': 'R130', 'Day': 'SAT', 'Hour': '10', 'Hourly Swipe': '32', 'Bucket': '1', 'Sample Set': '308'}]
