import os
import shutil
import pandas as pd

source_path = 'data/demo/'
dst_path = 'data/demo2'

files = ['SFECollectedData7', 'SFEGateComment3', 'SFEMain1', 'SupervisorSig']
dataList = list()

for file in files:
    try:
        data = pd.read_excel(source_path + str(file) + '.xlsx')
        # shutil.move(source_path + str(file), dst_path + str(file))
        dataList.append(data)
    except Exception as e:
        print(e)
        pass


print(len(dataList))
print(dataList)