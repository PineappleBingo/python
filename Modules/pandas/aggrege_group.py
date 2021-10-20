import pandas as pd

location = pd.read_csv("data/CSV/location.csv")


filt = location['state'] == 'New York'
print(location.loc[filt]['location_id'].value_counts())