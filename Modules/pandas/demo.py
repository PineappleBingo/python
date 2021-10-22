import pandas as pd

# from sqlalchemy import create_engine
# engine = create_engine("mysql+pymysql://root:little5@localhost:3306/k2")

# engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')
# engine = create_engine('oracle+cx_oracle://scott:tiger@tnsname')
# oracle+cx_oracle://user:pass@hostname:port[/dbname][?service_name=<service>[&key=value&key=value...]]

data = pd.read_excel("data/demo/SFECollectedData7.xlsx")
gate_comment = pd.read_excel("data/demo/SFEGateComment3.xlsx")
main = pd.read_excel("data/demo/SFEMain2.xlsx")
supervisor = pd.read_excel("data/demo/SupervisorSig.xlsx")

# print(data.head())
# print(gate_comment.head())
# print(main.head())
# print(supervisor.head())

# File loaded? 
# yes
# no - move the file to 'bucket'

files = ['SFECollectedData7', 'SFEGateComment3', 'SFEMain2', 'SupervisorSig']
dataList = list()

try:
    for file in files:
        with open("data/demo/" + file + ".xlsx", "r") as file:
            # Print the success message
            print(f"{file} has opened for reading")

except IOError:
    print("File has opened already.")

for file in files:
    data_in = pd.read_excel('data/demo/' + str(file) + '.xlsx')
    dataList.append(data_in)


print('success')
# print(dataList)
# print(dataList[0].shape)
# print(data.shape)

# print(gate_comment.shape)
# print(type(dataList))

# print(gate_comment.head())
# print(len(dataList))
# print(main.shape)
# print(dataList[3].shape)
# print(supervisor.shape)



# file open / fail

# Take the filename to check
# filename = input("Enter any existing filename:\n")
# Open the file for the first time using open() function
# fileHandler = open("data/demo/SFECollectedData7.xlsx", "r")
# Try to open the file same file again
# try:
#     with open("data/demo/SFECollectedData7.xlsx", "r") as file:
#         # Print the success message
#         print("File has opened for reading.")
#         data = pd.read_excel("data/demo/SFECollectedData7.xlsx")
#         print(data.head())

# except IOError:
#     print("File has opened already.")
    

# fileHandler.close()
# print("file closed")