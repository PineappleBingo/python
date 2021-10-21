import pandas as pd

xlsxdir = 'data/demo/'

try:
    data = pd.read_excel(xlsxdir + 'SFECollectedData7.xlsx')
    print(data.shape)
    print(data.head())
    
except Exception as e:
    print(e)