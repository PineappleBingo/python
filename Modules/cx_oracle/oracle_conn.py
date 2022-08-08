import cx_Oracle

# Oracle credentials
_USR = "admin"
_PWD = "SGlittle5^^^"
_DSN = "high"

try:
    connect = cx_Oracle.connect(user=_USR, password=_PWD, dsn=_DSN, encoding="UTF-8")
    print("----- DB connected -----")
    cursor = connect.cursor()
except cx_Oracle.Error as e:
    print("[Error] connecting to Oracle:", e)
    exit()
finally:
    print("----- DB disconnected -----")
    connect.close()
