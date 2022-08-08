from distutils.command.config import config
import cx_Oracle
import json
import os
import sys

sys.dont_write_bytecode = True
import traceback
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

db_con = None
sp_con = None

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PAR_DIR = os.path.abspath(os.path.join(ROOT_DIR, os.pardir))

try:
    config_path = "\\".join([ROOT_DIR, "config.json"])

    # Read config.json file
    with open(config_path) as config_file:
        db_config = json.load(config_file)
        db_config = db_config["oracle"]

    with open(config_path) as config_file:
        sp_config = json.load(config_file)
        sp_config = sp_config["share_point"]

    # Oracle Credientials
    m_strUserPass = db_config["user_pass"]
    DB_USERNAME = db_config["username"]
    DB_PASSWORD = db_config["password"]
    DB_DNS = db_config["dns"]

    # SharePoint Credentials
    SP_USERNAME = sp_config["username"]
    SP_PASSWORD = sp_config["password"]
    SHAREPOINT_URL = sp_config["site_url"]

    try:
        # Oracle DB connection Opt.1
        # account = m_strUserPass + "/" + m_strUserPass + "@xxxx.com:xxxx/xxxx"
        # db_con = cx_Oracle.connect(account)

        # Oracle DB connection Op5.2
        db_con = cx_Oracle.connect(
            user=DB_USERNAME, password=DB_PASSWORD, dsn=DB_DNS, encoding="UTF-8"
        )
        print("----- DB connected -----")
        cursor = db_con.cursor()

    except cx_Oracle.Error as e:
        print("[Error] connecting to Oracle:", e)
        db_con.close()

    try:
        # SharePoint Connection
        sp_con = ClientContext(SHAREPOINT_URL).with_credentials(
            UserCredential(SP_USERNAME, SP_PASSWORD)
        )
        print("----- SP connected -----")

    except Exception as e:
        print("[Error] connecting to SharePoint:", e)

    try:
        # do what you want
        print("---- your code here ----")

        # some_function1(db_con, sp_con, SP_list_name1)
        # some_function2(db_con, sp_con, SP_list_name2)

    except Exception as e:
        print("[Error]:", e)

    finally:
        print("---- DB Connection Closing ----")
        db_con.close()
        input("Press [Enter] to exit")

except Exception as e:
    print("Process Terminated: {}\n{}".format(e, traceback.format_exc()))
    input("Press [Enter] to exit")
