import csv
import os
import sys; sys.dont_write_bytecode = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = '\\'.join([ROOT_PATH, "sample.csv"])

with open(file_path) as file:
    csv_file = csv.DictReader(file, delimiter=",")
    # printing each row of table as dictionary 
    for row in csv_file:
        CHECKER_ID = row["CheckerNo"]
        DATA_KEY = row["DataKey"]
        OBSV_TIME = row["OBSV_TIME"]

        print(CHECKER_ID)
        print(DATA_KEY)
        print(OBSV_TIME)