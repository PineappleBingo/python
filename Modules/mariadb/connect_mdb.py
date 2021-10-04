import mariadb

# MariaDB credentials
_HST = '127.0.0.1'
_DBN = 'test'
_USR = 'root'
_PWD = ''

try:
    con = mariadb.connect(host = _HST, user = _USR, password = _PWD, database = _DBN)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    exit()

csr = con.cursor()
con.autocommit = False
            
con.commit()
print("----- DB connected -----")