import csv
import os
import sys

sys.dont_write_bytecode = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
IMPORT_PATH = os.path.join(ROOT_PATH, "Import")
EXPORT_PATH = os.path.join(ROOT_PATH, "Export")

file_in_path = "\\".join([IMPORT_PATH, "Sample.csv"])
file_out_path = "\\".join([EXPORT_PATH, "Output.csv"])

new_fileds = ["Sample Id", "Counts"]
new_rows = []


def IMPORT_CSV(file_in_path):
    try:
        with open(file_in_path) as file:
            csv_file = csv.DictReader(file, delimiter=",")
            # printing each row of table as dictionary
            for row in csv_file:
                SAMPLE_ID = row["Sample ID"]
                COUNTS = row["Counts"]

                new_rows.append({"Sample Id": SAMPLE_ID, "Counts": COUNTS})

    # If file not found
    except FileNotFoundError as e:
        print("[Error Mssg]:", e)
    except Exception as e:
        print("Not Processed: ", file_in_path, "[Error]:", e)


IMPORT_CSV(file_in_path)

with open(file_out_path, "w", encoding="UTF8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=new_fileds)
    writer.writeheader()
    writer.writerows(new_rows)
