import tkinter.scrolledtext as tkscrolled
from tkinter import filedialog as fd
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


class ExcelImportError(Exception):
    "Error occured while WeeeklySchedulePage.excel_to_csv() Run"
    pass


class MainApplication(tk.Tk):

    appWindow_w = 650
    appWindow_h = 408

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("SFE Schedule Template Converter")
        self.geometry("{}x{}".format(
            MainApplication.appWindow_w, MainApplication.appWindow_h))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage,
                  WeeeklySchedulePage,
                  QuarterlySamplePage
                  ):
            frame = F(container, self)
            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        """
        Switch Frames
        """
        frame = self.frames[cont]
        frame.tkraise()

    def close_app(self):
        """
        Close the application
        """
        self.quit()

    def set_ws_title(self):
        """
        Set Weekly Schedules Title
        """
        self.title("SFE Schedule Template Converter - Weekly Schedule")

    def set_qs_title(self):
        """
        Set Quarterly Schedule Title
        """
        self.title("SFE Schedule Template Converter - Quarterly Samples")

    def set_title(self):
        """
        Set the Application Title
        """
        self.title("SFE Schedule Template Converter")


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)

        open_ws_window_btn = tk.Button(
            button_frame,
            text="Weekly Schedule",
            height=5,
            width=23,
            command=lambda: [controller.show_frame(
                WeeeklySchedulePage), controller.set_ws_title()]
        )
        open_qs_window_btn = tk.Button(
            button_frame,
            height=5,
            width=23,
            text="Quarterly Samples",
            command=lambda: [controller.show_frame(
                QuarterlySamplePage), controller.set_qs_title()]
        )

        # User Interface
        name_label = tk.Label(self, text="SFE Schedule Template Converter",
                              font=('arial', 15))
        verion_label = tk.Label(self, text="version: 1.0.5")

        name_label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        button_frame.pack(padx=10, pady=10, expand=True, fill=tk.X)
        open_ws_window_btn.grid(row=0, column=1, sticky="e")
        open_qs_window_btn.grid(row=0, column=3, sticky="w")

        verion_label.pack(padx=10, pady=10)


class WeeeklySchedulePage(tk.Frame):

    IMPORT_PATH = None
    EXPORT_PATH = None
    CSV_PATH = None
    OP_FNAME = None
    imp_txt = None
    exp_txt = None
    op_txt = None

    ws_fileds = ["SSC Date", "SSC Start", "SSC End", "Checker", "Bus", "Job Number", "Job Code", "Job Name",
                 "Description", "Start Time", "End Time", "Depot", "Location", "Destination", "Rel Trip", "Checker Name"]
    ws_new_rows = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame_A = tk.Frame(
            self, width=MainApplication.appWindow_w)
        frame_AI = tk.Frame(frame_A)
        frame_A.grid(row=0, column=0, sticky="w")
        frame_AI.pack(pady=5, padx=5, expand=True, fill=tk.X)

        frame_AI.grid_columnconfigure(0, weight=1)
        frame_AI.grid_columnconfigure(1, weight=1)

        frame_B = tk.Frame(
            self, height=60, width=MainApplication.appWindow_w)
        frame_BI = tk.Frame(frame_B)
        frame_B.grid(row=1, column=0, sticky="w")
        frame_BI.place(
            x=5, y=5, width=MainApplication.appWindow_w-10, height=50)

        frame_BI.grid_columnconfigure(0, weight=1)
        frame_BI.grid_columnconfigure(1, weight=1)
        frame_BI.grid_columnconfigure(2, weight=1)
        frame_BI.grid_columnconfigure(3, weight=1)
        frame_BI.grid_columnconfigure(4, weight=1)
        frame_BI.grid_columnconfigure(5, weight=10)

        frame_C = tk.Frame(self)
        frame_CI = tk.Frame(frame_C, width=MainApplication.appWindow_w-40)
        frame_C.grid(row=2, column=0, sticky="w")
        frame_CI.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

        # Import Path
        tk.Label(frame_AI, text='Import Path', width=10).grid(
            row=0, column=0, sticky="w")
        imp_txt = tk.Text(frame_AI, height=1, width=70, wrap=tk.NONE)
        imp_txt.grid(row=0, column=1, sticky="w")
        # update class variable
        self.update_imp_txt(imp_txt)

        tk.Label(frame_AI, text='Export Path', width=10).grid(
            row=1, column=0, sticky="w")
        exp_txt = tk.Text(frame_AI, height=1, width=70, wrap=tk.NONE)
        exp_txt.grid(row=1, column=1, sticky="w")
        # update class variable
        self.update_exp_txt(exp_txt)

        # Rest Button
        reset_button = ttk.Button(
            frame_BI,
            text="Reset",
            command=self.reset_fields
        )
        # Import file open button
        import_button = ttk.Button(
            frame_BI,
            text='Open a File',
            command=self.import_ws_file
        )
        # Export path setup button
        export_button = ttk.Button(
            frame_BI,
            text='Set Export Path',
            command=self.set_export_path
        )
        # Convert execution button
        cnvrt_button = ttk.Button(
            frame_BI,
            text='Convert',
            command=self.convert_ws_file
        )
        exit_button = ttk.Button(frame_BI, text="Close",
                                 command=lambda: controller.close_app()
                                 )

        reset_button.grid(row=0, column=0, padx=3,
                          pady=15, ipadx=5, sticky="w")
        import_button.grid(row=0, column=1, padx=3,
                           pady=15, ipadx=10, sticky="w")
        export_button.grid(row=0, column=2, padx=3,
                           pady=15, ipadx=10, sticky="w")
        cnvrt_button.grid(row=0, column=3, padx=3,
                          pady=15, ipadx=10, sticky="w")
        exit_button.grid(row=0, column=5, padx=10,
                         pady=15, ipadx=5, sticky="e")

        op_txt = tkscrolled.ScrolledText(
            frame_CI,
            width=76, height=15,
            wrap=tk.WORD)
        op_txt.grid(row=0, column=0, padx=5, pady=5)
        # update class variable
        self.update_op_txt(op_txt)

        switch_window_button = tk.Button(
            self,
            text="Go to the Main Page",
            command=lambda: [controller.show_frame(
                MainPage), controller.set_title()]
        )
        switch_window_button.grid(row=3, column=0)

    def get_root_path(self):
        return r"\\\\transit\\nyct\\EVP_SHARE\\SDR_DATA\\Rzgrp\\P E S"

    def get_imp_path(self):
        return WeeeklySchedulePage.IMPORT_PATH

    def get_exp_path(self):
        return WeeeklySchedulePage.EXPORT_PATH

    def get_csv_path(self):
        return WeeeklySchedulePage.CSV_PATH

    def update_imp_path(self, new_path):
        WeeeklySchedulePage.IMPORT_PATH = new_path

    def update_exp_path(self, new_path):
        WeeeklySchedulePage.EXPORT_PATH = new_path

    def update_csv_path(self, new_path):
        WeeeklySchedulePage.CSV_PATH = new_path

    def get_fileds(self):
        return WeeeklySchedulePage.ws_fileds

    def get_new_rows(self):
        return WeeeklySchedulePage.ws_new_rows

    def update_imp_txt(self, value):
        WeeeklySchedulePage.imp_txt = value

    def update_exp_txt(self, value):
        WeeeklySchedulePage.exp_txt = value

    def update_op_txt(self, value):
        WeeeklySchedulePage.op_txt = value

    def get_imp_txt(self):
        return WeeeklySchedulePage.imp_txt

    def get_exp_txt(self):
        return WeeeklySchedulePage.exp_txt

    def get_op_txt(self):
        return WeeeklySchedulePage.op_txt

    def update_output_fname(self, filename):
        WeeeklySchedulePage.OP_FNAME = Path(filename).stem

    def get_output_fname(self):
        return WeeeklySchedulePage.OP_FNAME

    def reset_fields(self):
        """
        Reset the application
        """
        imp_txt = self.get_imp_txt()
        exp_txt = self.get_exp_txt()
        op_txt = self.get_op_txt()

        imp_txt.delete('1.0', tk.END)
        exp_txt.delete('1.0', tk.END)
        op_txt.delete('1.0', tk.END)

        self.update_imp_path(None)
        self.update_exp_path(None)

    def error_msg(self):
        """
        Display Exception in a messagebox
        """
        op_txt = self.get_op_txt()

        errlog_ts = str(datetime.datetime.now().strftime(
            "%m/%d/%Y %I:%M:%S %p "))
        err_message = traceback.format_exc()

        print("\n[Error]: An uncaught exception has occurred")
        print("\n", err_message)
        print("\n" + errlog_ts + " application terminating... ")
        op_txt.insert(tk.END, "\n[Error]: An uncaught exception has occurred")
        op_txt.insert(tk.END, "\n\n" + err_message)
        op_txt.insert(tk.END, "\n" + errlog_ts +
                      " Application terminating... ")

    def excel_to_csv(self, file_path):
        """
        Convert Excel file to CSV & .xlsx to .csv
        """
        isFailed = None

        try:
            # Convert .xlsx extion to .csv
            CSV_PATH = Path(file_path).with_suffix(".csv").as_posix()
            self.update_csv_path(CSV_PATH)

            df = pd.read_excel(file_path, sheet_name="AtcSched")

            # Change the data type float to Int64 leave NaN
            df["ASM_START_TIME"] = df["ASM_START_TIME"].astype("Int64")
            df["ASM_END_TIME"] = df["ASM_END_TIME"].astype("Int64")
            df["PES_START_TIME"] = df["PES_START_TIME"].astype("Int64")
            df["PES_END_TIME"] = df["PES_END_TIME"].astype("Int64")

            df.to_csv(CSV_PATH, index=None, header=True)

            isFailed = False
            return isFailed

        except FileNotFoundError:
            self.error_msg()
            isFailed = True
            return isFailed
        except BaseException:
            self.error_msg()
            isFailed = True
            return isFailed

    def import_ws_file(self):
        """
        Import Weekly Schedule CSV file
        """

        imp_txt = self.get_imp_txt()
        exp_txt = self.get_exp_txt()
        op_txt = self.get_op_txt()

        EXPORT_PATH = self.get_exp_path()
        IMPORT_PATH = self.get_imp_path()
        ROOT_PATH = self.get_root_path()

        implog_ts = str(datetime.datetime.now().strftime(
            "%m/%d/%Y %I:%M:%S %p "))

        filetypes = (
            ('Excel 97-2003 Workbook', '*.xls'),
            ('All files', '*.*')
        )
        # show the open file dialog
        impf = fd.askopenfile(
            filetypes=filetypes,
            initialdir=ROOT_PATH
            # r"\\\\transit\\nyct\\EVP_SHARE\\SDR_DATA\\Rzgrp\\P E S"
        )

        # Import file in path
        IMPORT_PATH = impf.name
        self.update_imp_path(IMPORT_PATH)
        # Import file name
        impf_name = Path(impf.name).name

        # Set input filename to class variable
        self.update_output_fname(impf_name)

        # Convert excel file to csv
        if self.excel_to_csv(IMPORT_PATH):
            raise ExcelImportError
        else:
            pass

        # Get updated CSV_PATH
        CSV_PATH = self.get_csv_path()

        # Pass if export path already set up by user
        if EXPORT_PATH is not None:
            pass
        else:
            SandBox_SubPath = Path(IMPORT_PATH).parent.name
            SandBox_Path = Path(IMPORT_PATH).parent.parent.joinpath(
                str("SANDBOX").upper()).joinpath("Weekly Schedules").joinpath(SandBox_SubPath)

            # # print("SandBox_Path:", SandBox_Path)
            # # print("SandBox_Path_posix:", Path(SandBox_Path).as_posix())

            # Set Default export file path to IMPORT_PATH.parent/SANSBOX/Weekly Schedule/{quarter}Q{year}
            if SandBox_Path.exists():
                self.update_exp_path(Path(SandBox_Path).as_posix())
                pass
            else:
                # if SandBox Path is not exist, creates folders by given path
                try:
                    self.update_exp_path(Path(SandBox_Path).as_posix())
                    SandBox_Path.mkdir(parents=True)

                except FileNotFoundError:
                    self.error_msg()
                except BaseException:
                    self.error_msg()

        # Reset Import/Export Path fields
        imp_txt.delete('1.0', tk.END)
        exp_txt.delete('1.0', tk.END)

        imp_txt.insert('1.0', IMPORT_PATH)
        exp_txt.insert('1.0', self.get_exp_path())

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

                    self.ws_new_rows.append(
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

            # print(self.ws_new_rows)

        except FileNotFoundError:
            self.error_msg()
        except BaseException:
            self.error_msg()

        else:
            print("\n" + implog_ts + impf_name + " Successfully Imported")
            op_txt.insert(tk.END, "\n" + implog_ts + impf_name +
                          " Successfully Imported")

    def set_export_path(self):
        """
        Set export path other than default path
        Default export path is set to import path

        """
        exp_txt = self.get_exp_txt()
        EXPORT_PATH = self.get_exp_path()
        ROOT_PATH = self.get_root_path()

        # show the open file dialog
        expf = fd.askdirectory(
            title="Export Directory",
            initialdir=ROOT_PATH
        )
        # read the csv file and show its name with path
        exp_txt.delete('1.0', tk.END)
        EXPORT_PATH = expf
        exp_txt.insert('1.0', EXPORT_PATH)

        # Set Export Path
        self.update_exp_path(expf)

    def convert_ws_file(self):
        """
        Export modified rows to CSV file
        """
        op_txt = self.get_op_txt()

        IMPORT_PATH = self.get_imp_path()
        EXPORT_PATH = self.get_exp_path()

        ws_fileds = self.get_fileds()
        ws_new_rows = self.get_new_rows()

        if IMPORT_PATH and EXPORT_PATH:

            expf_ts = str(datetime.datetime.now().strftime("%m%d%Y_%I%M%S"))
            explog_ts = str(datetime.datetime.now().strftime(
                "%m/%d/%Y %I:%M:%S %p "))

            OUTPUT_FNAME = self.get_output_fname()

            file_out_path = "/".join([str(EXPORT_PATH),
                                      (OUTPUT_FNAME + "_Weekly_Schedule_" + expf_ts + ".csv")])

            try:
                with open(file_out_path, "w", encoding="UTF8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=ws_fileds)
                    writer.writeheader()
                    writer.writerows(ws_new_rows)

            except BaseException:
                self.error_msg()

            else:
                print(
                    explog_ts + "File Successfully Converted & Exported!\n[File Path]: " + file_out_path)
                op_txt.insert(tk.END, "\n" + explog_ts +
                              "File Successfully Converted & Exported!")
                op_txt.insert(tk.END, "\n[File Path]: " + file_out_path)
                op_txt.insert(
                    tk.END, "\n-------------------------------------------------------------------------")

        elif IMPORT_PATH and EXPORT_PATH is None:
            op_txt.insert(tk.END, "\nPlease Select Export File Location")
            print("Please Select Export File Location")
        elif EXPORT_PATH and IMPORT_PATH is None:
            op_txt.insert(tk.END, "\nPlease Select Import File(.xlsx)")
            print("Please Select Import File")
        else:
            op_txt.insert(
                tk.END, "\nPlease Select Import File & Export File Location")
            print("Please Select Import File & Export File Location")


class QuarterlySamplePage(tk.Frame):

    IMPORT_PATH = None
    EXPORT_PATH = None
    OP_FNAME = None
    imp_txt = None
    exp_txt = None
    op_txt = None
    SAMPLE_NO = None

    qs_fileds = ["Sample ID", "Location", "Day",
                 "Hour", "Hourly Swipe", "Bucket", "Sample Set"]
    qs_new_rows = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame_A = tk.Frame(
            self, width=MainApplication.appWindow_w
            # , background="red"
        )
        frame_AI = tk.Frame(frame_A)
        frame_A.grid(row=0, column=0, sticky="w")
        frame_AI.pack(pady=5, padx=5, expand=True, fill=tk.X)

        frame_AI.grid_columnconfigure(0, weight=1)
        frame_AI.grid_columnconfigure(1, weight=1)

        frame_B = tk.Frame(
            self, height=60, width=MainApplication.appWindow_w
            # , background="blue"
        )
        frame_BI = tk.Frame(frame_B)
        frame_B.grid(row=1, column=0, sticky="w")
        frame_BI.place(
            x=5, y=5, width=MainApplication.appWindow_w-10, height=50)

        frame_BI.grid_columnconfigure(0, weight=1)
        frame_BI.grid_columnconfigure(1, weight=1)
        frame_BI.grid_columnconfigure(2, weight=1)
        frame_BI.grid_columnconfigure(3, weight=1)
        frame_BI.grid_columnconfigure(4, weight=1)
        frame_BI.grid_columnconfigure(5, weight=10)

        frame_C = tk.Frame(self
                           # , background="green"
                           )
        frame_CI = tk.Frame(frame_C, width=MainApplication.appWindow_w-40)
        frame_C.grid(row=2, column=0, sticky="w")
        frame_CI.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

        # Import Path
        tk.Label(frame_AI, text='Import Path', width=10).grid(
            row=0, column=0, sticky="w")
        imp_txt = tk.Text(frame_AI, height=1, width=70, wrap=tk.NONE)
        imp_txt.grid(row=0, column=1, sticky="w")
        # update class variable
        self.update_imp_txt(imp_txt)

        tk.Label(frame_AI, text='Export Path', width=10).grid(
            row=1, column=0, sticky="w")
        exp_txt = tk.Text(frame_AI, height=1, width=70, wrap=tk.NONE)
        exp_txt.grid(row=1, column=1, sticky="w")
        # update class variable
        self.update_exp_txt(exp_txt)

        # Rest Button
        reset_button = ttk.Button(
            frame_BI,
            text="Reset",
            command=self.reset_fields
        )
        # Import file open button
        import_button = ttk.Button(
            frame_BI,
            text='Open a File',
            command=self.import_qs_file
        )
        # Export path setup button
        export_button = ttk.Button(
            frame_BI,
            text='Set Export Path',
            command=self.set_export_path
        )
        # Convert execution button
        cnvrt_button = ttk.Button(
            frame_BI,
            text='Convert',
            command=self.convert_qs_file
        )
        exit_button = ttk.Button(frame_BI, text="Close",
                                 command=lambda: controller.close_app()
                                 )

        reset_button.grid(row=0, column=0, padx=3,
                          pady=15, ipadx=5, sticky="w")
        import_button.grid(row=0, column=1, padx=3,
                           pady=15, ipadx=10, sticky="w")
        export_button.grid(row=0, column=2, padx=3,
                           pady=15, ipadx=10, sticky="w")
        cnvrt_button.grid(row=0, column=3, padx=3,
                          pady=15, ipadx=10, sticky="w")
        exit_button.grid(row=0, column=5, padx=10,
                         pady=15, ipadx=5, sticky="e")

        op_txt = tkscrolled.ScrolledText(
            frame_CI,
            width=76, height=15,
            wrap=tk.WORD)
        op_txt.grid(row=0, column=0, padx=5, pady=5)
        # update class variable
        self.update_op_txt(op_txt)

        switch_window_button = tk.Button(
            self,
            text="Go to the Main Page",
            command=lambda: [controller.show_frame(
                MainPage), controller.set_title()]
        )
        switch_window_button.grid(row=3, column=0)

    def get_root_path(self):
        return r"\\\\transit\\nyct\\EVP_SHARE\\SDR_DATA\\Rzgrp\\P E S"

    def get_imp_path(self):
        return QuarterlySamplePage.IMPORT_PATH

    def get_exp_path(self):
        return QuarterlySamplePage.EXPORT_PATH

    def update_imp_path(self, new_path):
        QuarterlySamplePage.IMPORT_PATH = new_path

    def update_exp_path(self, new_path):
        QuarterlySamplePage.EXPORT_PATH = new_path

    def get_fileds(self):
        return QuarterlySamplePage.qs_fileds

    def get_new_rows(self):
        return QuarterlySamplePage.qs_new_rows

    def update_imp_txt(self, value):
        QuarterlySamplePage.imp_txt = value

    def update_exp_txt(self, value):
        QuarterlySamplePage.exp_txt = value

    def update_op_txt(self, value):
        QuarterlySamplePage.op_txt = value

    def get_imp_txt(self):
        return QuarterlySamplePage.imp_txt

    def get_exp_txt(self):
        return QuarterlySamplePage.exp_txt

    def get_op_txt(self):
        return QuarterlySamplePage.op_txt

    def update_sample_no(self, numb):
        QuarterlySamplePage.SAMPLE_NO = numb

    def get_sample_no(self):
        return QuarterlySamplePage.SAMPLE_NO

    def update_output_fname(self, filename):
        QuarterlySamplePage.OP_FNAME = Path(filename).stem

    def get_output_fname(self):
        return QuarterlySamplePage.OP_FNAME

    def reset_fields(self):
        """
        Reset Import/Export Fields and Path
        """
        imp_txt = self.get_imp_txt()
        exp_txt = self.get_exp_txt()
        op_txt = self.get_op_txt()

        imp_txt.delete('1.0', tk.END)
        exp_txt.delete('1.0', tk.END)
        op_txt.delete('1.0', tk.END)

        self.update_imp_path(None)
        self.update_exp_path(None)

    def error_msg(self):
        """
        Display Exception in a messagebox
        """
        op_txt = self.get_op_txt()

        errlog_ts = str(datetime.datetime.now().strftime(
            "%m/%d/%Y %I:%M:%S %p "))
        err_message = traceback.format_exc()

        print("\n[Error]: An uncaught exception has occurred")
        print("\n", err_message)
        print("\n" + errlog_ts + " application terminating... ")
        op_txt.insert(tk.END, "\n[Error]: An uncaught exception has occurred")
        op_txt.insert(tk.END, "\n\n" + err_message)
        op_txt.insert(tk.END, "\n" + errlog_ts +
                      " Application terminating... ")

    def import_qs_file(self):
        """
        Import Quarterly Schedule CSV file
        """
        imp_txt = self.get_imp_txt()
        exp_txt = self.get_exp_txt()
        op_txt = self.get_op_txt()

        IMPORT_PATH = self.get_imp_path()
        EXPORT_PATH = self.get_exp_path()
        ROOT_PATH = self.get_root_path()

        implog_ts = str(datetime.datetime.now().strftime(
            "%m/%d/%Y %I:%M:%S %p "))

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

        # Set input filename to class variable
        self.update_output_fname(impf_name)
        # update class variable
        self.update_imp_path(IMPORT_PATH)

        # Pass if export path already set up by user
        if EXPORT_PATH is not None:
            pass
        else:
            SandBox_SubPath = Path(IMPORT_PATH).parent.name
            SandBox_Path = Path(IMPORT_PATH).parent.parent.joinpath(
                str("SANDBOX").upper()).joinpath("Quarterly Samples").joinpath(SandBox_SubPath)

            # # print("SandBox_Path:", SandBox_Path)
            # # print("SandBox_Path_posix:", Path(SandBox_Path).as_posix())

            # Set Default export file path to IMPORT_PATH.parent/SANSBOX/Quarterly Samples/{quarter}Q{year}
            if SandBox_Path.exists():
                self.update_exp_path(Path(SandBox_Path).as_posix())
                pass
            else:
                # if SandBox Path is not exist, creates folders by given path
                try:
                    self.update_exp_path(Path(SandBox_Path).as_posix())
                    SandBox_Path.mkdir(parents=True)

                except FileNotFoundError:
                    self.error_msg()
                except BaseException:
                    self.error_msg()

        # Reset Import/Export Path fields
        imp_txt.delete('1.0', tk.END)
        exp_txt.delete('1.0', tk.END)

        imp_txt.insert('1.0', IMPORT_PATH)
        exp_txt.insert('1.0', self.get_exp_path())

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

                    self.qs_new_rows.append(
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

                    # Set Sample No
                    self.update_sample_no(SAMPLE_SET)

        except FileNotFoundError:
            print("error")
            self.error_msg()
        except BaseException:
            self.error_msg()
            print("error")
        else:
            print("\n" + implog_ts + impf_name + " Successfully Imported")
            op_txt.insert(tk.END, "\n" + implog_ts +
                          impf_name + " Successfully Imported")

    def set_export_path(self):
        """
        Set export path other than default path
        Default export path is set to import path

        """
        exp_txt = self.get_exp_txt()

        EXPORT_PATH = self.get_exp_path()
        ROOT_PATH = self.get_root_path()

        # show the open file dialog
        expf = fd.askdirectory(
            title="Export Directory",
            initialdir=ROOT_PATH
        )
        # read the csv file and show its name with path
        exp_txt.delete('1.0', tk.END)
        EXPORT_PATH = expf
        exp_txt.insert('1.0', EXPORT_PATH)

        # Set Export Path
        self.update_exp_path(expf)

    def convert_qs_file(self):
        """
        Export modified rows to CSV file
        """

        op_txt = self.get_op_txt()
        qs_fileds = self.get_fileds()
        qs_new_rows = self.get_new_rows()

        IMPORT_PATH = self.get_imp_path()
        EXPORT_PATH = self.get_exp_path()

        if IMPORT_PATH and EXPORT_PATH:

            expf_ts = str(datetime.datetime.now().strftime("%m%d%Y_%I%M%S"))
            explog_ts = str(datetime.datetime.now().strftime(
                "%m/%d/%Y %I:%M:%S %p "))

            OUTPUT_FNAME = self.get_output_fname()

            file_out_path = "/".join([str(EXPORT_PATH),
                                      (OUTPUT_FNAME + "_" + str(self.get_sample_no()) + "_" + expf_ts + ".csv")])

            try:
                with open(file_out_path, "w", encoding="UTF8", newline="") as f:
                    writer = csv.DictWriter(
                        f, fieldnames=qs_fileds)
                    writer.writeheader()
                    writer.writerows(qs_new_rows)

            except BaseException:
                self.error_msg()

            else:
                print(
                    explog_ts + "File Successfully Converted & Exported!\n[File Path]: " + file_out_path)
                op_txt.insert(tk.END, "\n" + explog_ts +
                              "File Successfully Converted & Exported!")
                op_txt.insert(tk.END, "\n[File Path]: " + file_out_path)
                op_txt.insert(
                    tk.END, "\n-------------------------------------------------------------------------")

        elif IMPORT_PATH and EXPORT_PATH is None:

            op_txt.insert(tk.END, "\nPlease Select Export File Location")
            print("Please Select Export File Location")
        elif EXPORT_PATH and IMPORT_PATH is None:
            op_txt.insert(tk.END, "\nPlease Select Import File(.csv)")
            print("Please Select Import File")
        else:
            op_txt.insert(
                tk.END, "\nPlease Select Import File & Export File Location")
            print("Please Select Import File & Export File Location")


if __name__ == "__main__":
    testObj = MainApplication()
    testObj.mainloop()


# print(new_rows)
# [{'Sample ID': 'N308SAT1000000', 'Location': 'R507', 'Day': 'SAT', 'Hour': '12', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000001', 'Location': 'C11', 'Day': 'SAT', 'Hour': '13', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000002', 'Location': 'R130', 'Day': 'SAT', 'Hour': '10', 'Hourly Swipe': '32', 'Bucket': '1', 'Sample Set': '308'}]
