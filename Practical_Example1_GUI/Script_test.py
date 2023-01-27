import tkinter.scrolledtext as tkscrolled
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


class MainApplication(tk.Tk):

    appWindow_w = 650
    appWindow_h = 408

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("SFE Schedule Template Converter")
        self.geometry("{}x{}".format(self.appWindow_w, self.appWindow_h))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, QuarterlySchedulePage, WeeeklySchedulePage):
            # Generators
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
            command=lambda: controller.show_frame(WeeeklySchedulePage)
        )
        open_qs_window_btn = tk.Button(
            button_frame,
            height=5,
            width=23,
            text="Quarterly Schedule",
            command=lambda: controller.show_frame(QuarterlySchedulePage)
        )

        # User Interface
        name_label = tk.Label(self, text="SFE Schedule Template Converter",
                              font=('arial', 15))
        verion_label = tk.Label(self, text="version: 1.0.2")

        name_label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        button_frame.pack(padx=10, pady=10, expand=True, fill=tk.X)
        open_ws_window_btn.grid(row=0, column=1, sticky="e")
        open_qs_window_btn.grid(row=0, column=3, sticky="w")

        verion_label.pack(padx=10, pady=10)


class WeeeklySchedulePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Another Frame structure
        frame_A = tk.Frame(self, width=100, height=100, background="red")
        # frame_AI = tk.Frame(frame_A, width=100, background="yellow")
        frame_A.grid(row=1, column=0)

        label1 = tk.Label(frame_A, text="Weekely Schedule")
        label1.pack(padx=10, pady=10)

        label2 = tk.Label(self, text="bottom")
        label2.grid(row=2, column=0)

        # label = tk.Label(self, text="This is the Side Page")
        # label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Main Page",
            command=lambda: controller.show_frame(MainPage),
        )
        # switch_window_button.pack(side="bottom", fill=tk.X)
        switch_window_button.grid(row=3, column=0)


class QuarterlySchedulePage(tk.Frame):

    IMPORT_PATH = None
    EXPORT_PATH = None
    # CSV_PATH = None
    imp_txt = None
    exp_txt = None
    op_text = None

    qs_fileds = ["Sample ID", "Location", "Day",
                 "Hour", "Hourly Swipe", "Bucket", "Sample Set"]
    qs_new_rows = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # pass tkinter objets to class variables
        global imp_txt
        global exp_txt
        global op_text

        frame_A = tk.Frame(
            self, width=MainApplication.appWindow_w, background="red")
        frame_AI = tk.Frame(frame_A)
        frame_A.grid(row=0, column=0, sticky="w")
        frame_AI.pack(pady=5, padx=5, expand=True, fill=tk.X)

        frame_AI.grid_columnconfigure(0, weight=1)
        frame_AI.grid_columnconfigure(1, weight=1)

        frame_B = tk.Frame(
            self, height=60, width=MainApplication.appWindow_w, background="blue")
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

        frame_C = tk.Frame(self, background="green")
        frame_CI = tk.Frame(frame_C, width=MainApplication.appWindow_w-40)
        frame_C.grid(row=2, column=0, sticky="w")
        frame_CI.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

        # Import Path
        tk.Label(frame_AI, text='Import Path', width=10).grid(
            row=0, column=0, sticky="w")
        imp_txt = tk.Text(frame_AI, height=1, width=70, wrap=tk.NONE)
        imp_txt.grid(row=0, column=1, sticky="w")

        tk.Label(frame_AI, text='Export Path', width=10).grid(
            row=1, column=0, sticky="w")
        exp_txt = tk.Text(frame_AI, height=1, width=70, wrap=tk.NONE)
        exp_txt.grid(row=1, column=1, sticky="w")

        # Import file open button
        import_qs_button = ttk.Button(
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
        cnvrt_qs_button = ttk.Button(
            frame_BI,
            text='Convert',
            command=self.convert_qs_file
        )
        exit_button = ttk.Button(frame_BI, text="Close",
                                 command=lambda: controller.close_app()
                                 )

        import_qs_button.grid(row=0, column=0, padx=3,
                              pady=15, ipadx=10, sticky="w")
        export_button.grid(row=0, column=1, padx=3,
                           pady=15, ipadx=10, sticky="w")
        cnvrt_qs_button.grid(row=0, column=2, padx=3,
                             pady=15, ipadx=20, sticky="w")
        exit_button.grid(row=0, column=5, padx=10,
                         pady=15, ipadx=5, sticky="e")

        op_text = tkscrolled.ScrolledText(
            frame_CI,
            width=76, height=15,
            wrap=tk.WORD)
        op_text.grid(row=0, column=0, padx=5, pady=5)

        switch_window_button = tk.Button(
            self,
            text="Go to the Main Page",
            command=lambda: controller.show_frame(MainPage),
        )
        switch_window_button.grid(row=3, column=0)

    def get_root_path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def get_imp_path(self):
        return QuarterlySchedulePage.IMPORT_PATH

    def get_exp_path(self):
        return QuarterlySchedulePage.EXPORT_PATH

    def update_imp_path(self, new_path):
        QuarterlySchedulePage.IMPORT_PATH = new_path

    def update_exp_path(self, new_path):
        QuarterlySchedulePage.EXPORT_PATH = new_path

    def reset_fields(self):
        """
        Reset the application
        """
        # inherite class variable
        self.imp_txt = QuarterlySchedulePage.imp_txt
        self.exp_txt = QuarterlySchedulePage.exp_txt
        self.op_text = QuarterlySchedulePage.op_text

        imp_txt.delete('1.0', tk.END)
        exp_txt.delete('1.0', tk.END)
        op_text.delete('1.0', tk.END)

    def error_msg(self):
        """
        Display Exception in a messagebox
        """
        self.imp_txt = QuarterlySchedulePage.imp_txt
        self.exp_txt = QuarterlySchedulePage.exp_txt
        self.op_text = QuarterlySchedulePage.op_text

        errlog_ts = str(datetime.datetime.now().strftime(
            "%m/%d/%Y %I:%M:%S %p "))
        err_message = traceback.format_exc()

        print("\n[Error]: An uncaught exception has occurred")
        print("\n", err_message)
        print("\n" + errlog_ts + " application terminating... ")
        op_text.insert('1.0', "[Error]: An uncaught exception has occurred")
        op_text.insert(tk.END, "\n\n" + err_message)
        op_text.insert(tk.END, "\n" + errlog_ts +
                       " Application terminating... ")

    def import_qs_file(self):
        """
        Import Quarterly Schedule CSV file
        """

        # inherite class variable
        self.imp_txt = QuarterlySchedulePage.imp_txt
        self.exp_txt = QuarterlySchedulePage.exp_txt
        self.op_text = QuarterlySchedulePage.op_text

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
        # update class variable
        self.update_imp_path(IMPORT_PATH)

        # Pass if export path already set up by user
        if EXPORT_PATH is not None:
            print("EXPORT_PATH:", EXPORT_PATH)
            pass
        else:
            # Set Default export file path same as import file location
            self.update_exp_path(Path(impf.name).parent.as_posix())

        # Reset text fields once user click "Open File" again.
        self.reset_fields()

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

        except FileNotFoundError:
            print("error")
            self.error_msg()
        except BaseException:
            self.error_msg()
            print("error")
        else:
            print("\n" + implog_ts + impf_name + " Successfully Imported")
            op_text.insert('1.0', implog_ts +
                           impf_name + " Successfully Imported")

    def set_export_path(self):
        """
        Set export path other than default path
        Default export path is set to import path

        """
        self.exp_txt = QuarterlySchedulePage.exp_txt

        EXPORT_PATH = self.get_exp_path()

        # show the open file dialog
        expf = fd.askdirectory(
            title="Export Directory"
            # initialdir = os.getcwd()
        )
        # read the csv file and show its name with path
        exp_txt.delete('1.0', tk.END)
        EXPORT_PATH = expf
        exp_txt.insert('1.0', EXPORT_PATH)

        self.update_exp_path(expf)
        print("EXPORT_PATH_SET_TO:", EXPORT_PATH)
        print("EXPORT_PATH_SET_TO:", self.get_exp_path())

    def convert_qs_file(self):
        """
        Export modified rows to CSV file
        """
        self.imp_txt = QuarterlySchedulePage.imp_txt
        self.exp_txt = QuarterlySchedulePage.exp_txt
        self.op_text = QuarterlySchedulePage.op_text

        IMPORT_PATH = self.get_imp_path()
        EXPORT_PATH = self.get_exp_path()

        qs_fileds = QuarterlySchedulePage.qs_fileds
        qs_new_rows = QuarterlySchedulePage.qs_new_rows

        if IMPORT_PATH and EXPORT_PATH:

            expf_ts = str(datetime.datetime.now().strftime("%m%d%Y_%I%M%S"))
            explog_ts = str(datetime.datetime.now().strftime(
                "%m/%d/%Y %I:%M:%S %p "))

            file_out_path = "/".join([str(EXPORT_PATH),
                                      ("sample_308_schedule_output_" + expf_ts + ".csv")])

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


if __name__ == "__main__":
    testObj = MainApplication()
    testObj.mainloop()


# print(new_rows)
# [{'Sample ID': 'N308SAT1000000', 'Location': 'R507', 'Day': 'SAT', 'Hour': '12', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000001', 'Location': 'C11', 'Day': 'SAT', 'Hour': '13', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000002', 'Location': 'R130', 'Day': 'SAT', 'Hour': '10', 'Hourly Swipe': '32', 'Bucket': '1', 'Sample Set': '308'}]
