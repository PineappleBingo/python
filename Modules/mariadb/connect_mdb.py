import mariadb

# MariaDB credentials
_HST = '127.0.0.1'
_DBN = 'test'
_USR = 'root'
_PWD = 'little5'

try:
    con = mariadb.connect(host = _HST, user = _USR, password = _PWD, database = _DBN)
    print("----- DB connected -----")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    exit()

csr = con.cursor()
con.autocommit = False
             
# try:
    
#     for TBL in TBLS:
#         csr.execute(f'DELETE FROM all_{TBL};')
#         # csr.execute(f'CREATE TABLE IF NOT EXISTS all_{TBL} LIKE {TBL};')
#         csr.execute(f'INSERT INTO all_{TBL} SELECT * FROM {TBL}')
    
# except mariadb.Error as e:
#     print(f"Error Inserting to MariaDB: {e}")
#     con.rollback()
#     con.close()
#     exit()
            
con.commit()
