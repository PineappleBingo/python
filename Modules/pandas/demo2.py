import pandas as pd

xlsxdir = 'data/demo/'
files = ['SFECollectedData7', 'SFEGateComment3', 'SFEMain2', 'SupervisorSig']
dataList = list()

for file in files:
    try:
        data = pd.read_excel(xlsxdir + str(file) + '.xlsx')
    except Exception as e:
        print(e)

    
    