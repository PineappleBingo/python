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

files = ['SFECollectedData7', 'SFEGateComment3', 'SFEMain1', 'SupervisorSig']
dataList = list()

for file in files:
    try:
        with open("data/demo/" + file + ".xlsx", "r") as file:
            # Print the success message
            print(f"{file} has opened for reading")
            
    except IOError as e:
        print(e)
