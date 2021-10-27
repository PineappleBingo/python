import os
import shutil
import pandas as pd
import json
from sqlalchemy import create_engine
from sqlalchemy.engine.create import engine_from_config

engine = create_engine("mysql+pymysql://root:little5@localhost:3306/mta")

source_path = 'data/demo/'
dst_path = 'data/demo2'

files = ['SFECollectedData7', 'SFEGateComment3', 'SFEMain2', 'SupervisorSig']
dataList = list()

for file in files:
    try:
        data = pd.read_excel(source_path + str(file) + '.xlsx')
        dataList.append(data)
    except Exception as e:
        print(e)
        # dest = shutil.move(source_path + str(file), dst_path + str(file))
        # print("File moved to : ", dest)

read_comment = dataList[1]
print(read_comment.head())



# query execution 
# for rw in rws:
#     csr.execute('insert into \"all_' + _TBL + '\" values(' + str(rw)[1:-1] + ');')


# mdb data connection made
# comment = pd.read_sql('select * from sfe_comment', engine)
# print(comment)

col = ['TimePeriod', 'SeqNo', 'JobNo', 'Comment', 'Count', 'OBSV_TIME', '__PowerAppsId__']

print(read_comment.index)
# print(read_comment.agg(tuple, axis=1).tolist())

commentList = read_comment.agg(tuple, axis=1).tolist()
print(commentList[0])

# for index in read_comment.index:
#     print(read_comment[['SeqNo','JobNo']][index])
    # print ("df[" + str(index) + "] = " + str(read_comment.columns[col]))



# for rw in rws:
#     csr.execute('insert into all_' + _TBL + ' values(' + str(rw)[1:-1] + ');')


# reference 
# https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas