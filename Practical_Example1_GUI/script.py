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


# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo

# # filename = fd.askopenfilename()
# app = tk.Tk()
# app.title('Tkinter Open File Dialog')
# app.resizable(False, False)
# app.geometry('300x150')

# def select_file():
#     filetypes = (
#         ('CSV files', '*.csv')
#     )

#     filename = fd.askopenfilename(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes)

#     showinfo(
#         title='Selected File',
#         message=filename
#     )

# # open button
# open_button = ttk.Button(
#     app,
#     text='Open a File',
#     command=select_file
# )

# open_button.pack(expand=True)


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


# Root window
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('600x250')

# Import Path
imp_txt = tk.Text(root, height=1)
imp_txt.grid(row=0, column=1, sticky="nsew")

tk.Label(root, text='Import Path').grid(row=0)
tk.Label(root, text='Export Path').grid(row=1)

exp_txt = tk.Text(root, height=1)
exp_txt.grid(row=1, column=1, sticky="nsew")


def import_file():
    # file type
    filetypes = (
        ('CSV files', '*.csv'),
        ('All files', '*.*')
    )
    # show the open file dialog
    impf = fd.askopenfile(
        filetypes=filetypes, 
        initialdir = os.getcwd())

    # read the csv file and show its name with path
    imp_txt.insert('1.0', impf.name)

def export_file():
    # file type
    # filetypes = (
    #     ('CSV files', '*.csv'),
    #     ('All files', '*.*')
    # )
    # show the open file dialog
    expf = fd.askdirectory(
        # filetypes=filetypes, 
        # initialdir = os.getcwd()
        )

    # read the csv file and show its name with path
    exp_txt.insert('1.0', expf.folderPath)


# import file button
import_button = ttk.Button(
    root,
    text='Open a File',
    command=import_file
)

# export file button
export_button = ttk.Button(
    root,
    text='Open a File',
    command=export_file
)


import_button.grid(column=0, row=2, sticky='w', padx=10, pady=10)
export_button.grid(column=1, row=2, sticky='w', padx=10, pady=10)


root.mainloop()



# tk.Label(app, text='Import Path').grid(row=1)
# tk.Label(app, text='Export Path').grid(row=2)
# IFP = tk.Entry(app, width=70)
# EFP = tk.Entry(app, width=70)

# IFP.grid(row=1, column=1)
# EFP.grid(row=2, column=1)

# IFP_Btn = tk.Button(app, text="Open")
# EFP_Btn = tk.Button(app, text="Open")

# IFP_Btn.grid(row=1, column=2)
# EFP_Btn.grid(row=2, column=2)

# ourMessage ='This is our Message'
# messageVar = tk.Message(app, text = ourMessage)

# messageVar.config(bg='lightgreen')
# messageVar.grid(row=3)

# app.mainloop()

# https://realpython.com/python-gui-tkinter/


# print(new_rows)
# [{'Sample Id': 'N3080000001', 'Counts': '10', 'Control Area': '308'},
#  {'Sample Id': 'N3070000002', 'Counts': '20', 'Control Area': '307'},
#  {'Sample Id': 'Q1350000003', 'Counts': '30', 'Control Area': '135'},
#  {'Sample Id': 'Q1500000004', 'Counts': '40', 'Control Area': '150'}]



# from tkinter import *
# class MyWindow:
#     def __init__(self, win):
#         self.lbl1=Label(win, text='First number')
#         self.lbl2=Label(win, text='Second number')
#         self.lbl3=Label(win, text='Result')
#         self.t1=Entry(bd=3)
#         self.t2=Entry()
#         self.t3=Entry()
#         self.btn1 = Button(win, text='Add')
#         self.btn2=Button(win, text='Subtract')
#         self.lbl1.place(x=100, y=50)
#         self.t1.place(x=200, y=50)
#         self.lbl2.place(x=100, y=100)
#         self.t2.place(x=200, y=100)
#         self.b1=Button(win, text='Add', command=self.add)
#         self.b2=Button(win, text='Subtract')
#         self.b2.bind('<Button-1>', self.sub)
#         self.b1.place(x=100, y=150)
#         self.b2.place(x=200, y=150)
#         self.lbl3.place(x=100, y=200)
#         self.t3.place(x=200, y=200)
#     def add(self):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get())
#         num2=int(self.t2.get())
#         result=num1+num2
#         self.t3.insert(END, str(result))
#     def sub(self, event):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get())
#         num2=int(self.t2.get())
#         result=num1-num2
#         self.t3.insert(END, str(result))

# window=Tk()
# mywin=MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.mainloop()