# ----------------------------------
# Open Json file
# ----------------------------------
import os
import json

# filepath = os.getcwd()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = '\\'.join([ROOT_DIR, "config.json"])

# Read config.json file
with open(config_path) as config_file:
    sp_config = json.load(config_file)
    sp_config = sp_config["share_point"]

# print(sp_config)
# {'username': 'your_ID@nyct.com', 'password': 'your_password', 'site_url': 'https://nymta.sharepoint.com/sites/SFEFiles2/'}
    
# SharePoint credentials
SP_USERNAME = sp_config["username"]
SP_PASSWORD = sp_config["password"]
SHAREPOINT_URL = sp_config["site_url"]

print(SP_USERNAME)
print(SP_PASSWORD)
print(SHAREPOINT_URL)

