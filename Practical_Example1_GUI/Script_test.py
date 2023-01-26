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


import tkinter as tk

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
       
        self.title("test application")
        self.geometry('658x350')

        container = tk.Frame(self, height=500, width=500, background="red")
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)
        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        labela = tk.Label(master=container, text="hi", background="yellow")
        labela.pack()

        container.pack_propagate(0)

        # We will now create a dictionary of frames
        self.frames = {}

        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SidePage):
            # Generators
            frame = F(container, self)
            print("frame:", frame)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            print(self.frames[F])
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)
        
        print("self.frames:", self.frames)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Another Frame structure

        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10) 

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Another Frame structure
        
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Main Page",
            command=lambda: controller.show_frame(MainPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    testObj = MainApplication()
    testObj.mainloop()



# import tkinter as tk

# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)

# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#     def close_windows(self):
#         self.master.destroy()

# def main(): 
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()

# if __name__ == '__main__':
#     main()





# class windows(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.wm_title("test application")
        
#         # creating a frame and assigning it to container
#         container = tk.Frame(self, height=400, width=600)
#         # specifying the region where the frame is packed in root
#         container.pack(side="top", fill="both", expand=True)

#         # configuring the location of the container using grid
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         # We will now create a dictionary of frames
#         self.frames = {}
#         # we'll create the frames themselves later but let's add the components to the dictionary.
#         for F in (MainPage, SidePage, CompletionScreen):
#             print(F)
#             frame = F(container, self)
#             print("frame:", frame)

#             # the windows class acts as the root window for the frames.
#             self.frames[F] = frame
#             print(self.frames[F])
#             frame.grid(row=0, column=0, sticky="nsew")

#         # Using a method to switch frames
#         self.show_frame(MainPage)

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         # raises the current frame to the top
#         frame.tkraise()


# class MainPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Main Page")
#         label.pack(padx=10, pady=10)

#         # We use the switch_window_button in order to call the show_frame() method as a lambda function
#         switch_window_button = tk.Button(
#             self,
#             text="Go to the Side Page",
#             command=lambda: controller.show_frame(SidePage),
#         )
#         switch_window_button.pack(side="bottom", fill=tk.X)


# class SidePage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="This is the Side Page")
#         label.pack(padx=10, pady=10)

#         switch_window_button = tk.Button(
#             self,
#             text="Go to the Completion Screen",
#             command=lambda: controller.show_frame(CompletionScreen),
#         )
#         switch_window_button.pack(side="bottom", fill=tk.X)


# class CompletionScreen(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Completion Screen, we did it!")
#         label.pack(padx=10, pady=10)
#         switch_window_button = ttk.Button(
#             self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
#         )
#         switch_window_button.pack(side="bottom", fill=tk.X)


# if __name__ == "__main__":
#     testObj = windows()
#     testObj.mainloop()





# def close():
#     app.quit()

# def import_file():
#     """
#     Import CSV file

#     """
#     global EXPORT_PATH

#     filetypes = (
#         ('CSV files', '*.csv'),
#         ('All files', '*.*')
#     )
#     # show the open file dialog
#     impf = fd.askopenfile(
#         filetypes=filetypes,
#         initialdir=ROOT_PATH)

#     # Import file in path
#     IMPORT_FILE = impf.name
#     # Import file name
#     impf_name = Path(impf.name).name
#     # Set Default export file path same as import file path
#     EXPORT_PATH = Path(impf.name).parent.as_posix()
    
#     imp_txt.delete('1.0', tk.END)
#     exp_txt.delete('1.0', tk.END)
#     op_text.delete('1.0', tk.END)

#     imp_txt.insert('1.0', IMPORT_FILE)
#     exp_txt.insert('1.0', EXPORT_PATH)

#     try:
#         with open(IMPORT_FILE) as file:
#             csv_file = csv.DictReader(file, delimiter=",")
#             # Read CSV rows and generates new format to export
#             for row in csv_file:
#                 SAMPLE_ID = row["sample_id"]
#                 LOCATION = row["loc"]
#                 DAY = row["day_type"]
#                 HOUR = row["begin_time"]
#                 HOURLY_SWIPE = row["swipes"]
#                 BUCKET = row["strata"]
#                 SAMPLE_SET = str(row["sample_id"])[1:4]

#                 new_rows.append(
#                     {
#                         "Sample ID": SAMPLE_ID,
#                         "Location": LOCATION,
#                         "Day": DAY,
#                         "Hour": HOUR,
#                         "Hourly Swipe": HOURLY_SWIPE,
#                         "Bucket": BUCKET,
#                         "Sample Set": SAMPLE_SET,
#                     }
#                 )

#     except FileNotFoundError as e:
#         print("\n[Error]:", e)
#         op_text.insert('1.0', e)
#     except BaseException as e:
#         print("\n[Error]:", e)
#         op_text.insert('1.0', e)
#     else:
#         print("\n" + impf_name + " Successfully Imported")
#         # op_text.insert('1.0', impf_name + "File Successfully Imported")
#         op_text.insert('1.0', "File Successfully Imported")



# def set_export_path():
#     """
#     Set export path other than default path
#     Default export path is set to import path
    
#     """
#     global EXPORT_PATH
#     # show the open file dialog
#     expf = fd.askdirectory(
#         title="Export Directory"
#         # initialdir = os.getcwd()
#     )
#     # read the csv file and show its name with path
#     exp_txt.delete('1.0', tk.END)
#     EXPORT_PATH = expf
#     exp_txt.insert('1.0', EXPORT_PATH)


# def convert_file():
#     """
#     Export modified rows to CSV file

#     """
#     if EXPORT_PATH :
        
#         ts = str(datetime.datetime.now().strftime("%m%d%Y_%I%M%S"))
#         file_out_path = "/".join([str(EXPORT_PATH), ("sample_308_schedule_output_" + ts +".csv")])
        
#         try:
#             with open(file_out_path, "w", encoding="UTF8", newline="") as f:
#                 writer = csv.DictWriter(f, fieldnames=new_fileds)
#                 writer.writeheader()
#                 writer.writerows(new_rows)

#         except BaseException as e:
#             print("\nNot Processed: ", file_out_path, "[Error]:", e)
#             op_text.insert(tk.END, "\n" + e)      
#             # logging.exception(e)
#         else:
#             print("File Successfully Converted & Exported!\n[File Path]: " + file_out_path)
#             op_text.insert(tk.END, "\nFile Successfully Converted & Exported!\n[File Path]: " + file_out_path)
#             # logging.info(
#             #     "File Successfully Exported!\n[File Path]: " + file_out_path)

#     else:
#         op_text.insert(tk.END, "\nPlease select export file location")
#         print("Please select export file location")
    

# # App window
# app = tk.Tk()
# app.title('SFE Schedule Template Converter')
# app.resizable(False, False)
# app.geometry('658x350')

# # Import Path
# imp_txt = tk.Text(app, height=1, width=70, wrap=tk.NONE)
# imp_txt.grid(row=0, column=1, columnspan=4)

# tk.Label(app, text='Import Path').grid(row=0, column=0, pady=2)
# tk.Label(app, text='Export Path').grid(row=1, column=0)

# exp_txt = tk.Text(app, height=1, width=70, wrap=tk.NONE)
# exp_txt.grid(row=1, column=1, columnspan=4)

# # import file button
# import_button = ttk.Button(
#     app,
#     text='Open a File',
#     command=import_file
# )
# # export file button
# export_button = ttk.Button(
#     app,
#     text='Set Export Path',
#     command=set_export_path
# )

# cnvrt_button = ttk.Button(
#     app,
#     text='Convert',
#     command=convert_file
# )

# exit_button = ttk.Button(app, text="Close", command=close)

# import_button.grid(column=0, row=2, padx=3, pady=15)
# export_button.grid(column=1, row=2, padx=3, pady=15)
# cnvrt_button.grid(column=2, row=2, padx=3, pady=15, sticky="w")
# exit_button.grid(column=3, row=2, padx=10, pady=15, sticky="e")

# op_text = tk.Text(app, height=15, wrap=tk.WORD)
# op_text.grid(row=3, column=0, columnspan=4, padx=5, pady=10)

# app.mainloop()


# print(new_rows)
# [{'Sample ID': 'N308SAT1000000', 'Location': 'R507', 'Day': 'SAT', 'Hour': '12', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000001', 'Location': 'C11', 'Day': 'SAT', 'Hour': '13', 'Hourly Swipe': '52', 'Bucket': '1', 'Sample Set': '308'},
# {'Sample ID': 'N308SAT1000002', 'Location': 'R130', 'Day': 'SAT', 'Hour': '10', 'Hourly Swipe': '32', 'Bucket': '1', 'Sample Set': '308'}]
