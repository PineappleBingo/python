import pandas as pd  # importing pandas to write SharePoint list in excel or csv
from shareplum import Site
from requests_ntlm import HttpNtlmAuth

cred = HttpNtlmAuth("jinhodavid.seo@nyct.com", "SSlittle5^^")
site = Site("https://nymta.sharepoint.com/sites/SFEFiles2", auth=cred)

sp_list = site.List("SFECollectedData7")  # this creates SharePlum object
data = sp_list.GetListItems("All Items")  # this will retrieve all items from list

# this creates pandas data` frame you can perform any operation you like do within
# pandas capabilities

data_df = pd.DataFrame(data[0:])
print(data_df.head(5))
# data_df.to_csv("data.csv")`
