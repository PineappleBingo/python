import csv
import os
import sys

sys.dont_write_bytecode = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
file_out_path = "\\".join([ROOT_PATH, "outcome.csv"])


new_fileds = ["Sample Id", "Counts", "Control Area"]
new_rows = [
    {"Sample Id": "N3080000001", "Counts": "10", "Control Area": "308"},
    {"Sample Id": "N3070000002", "Counts": "20", "Control Area": "307"},
    {"Sample Id": "Q1350000003", "Counts": "30", "Control Area": "135"},
    {"Sample Id": "Q1500000004", "Counts": "40", "Control Area": "150"},
]

try:
    with open(file_out_path, "w", encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=new_fileds)
        writer.writeheader()
        writer.writerows(new_rows)

except Exception as e:
    print("Not Processed: ", file_out_path, "[Error]:", e)
