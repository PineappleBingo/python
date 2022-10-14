from datetime import datetime

# start time and end time
start_time = datetime.strptime("2:13:57", "%H:%M:%S")
end_time = datetime.strptime("11:46:38", "%H:%M:%S")

# get difference
delta = end_time - start_time

# # time difference in seconds
# print(f"Time difference is {delta.total_seconds()} seconds")

# time difference in milliseconds
ms = delta.total_seconds() * 1000
print(f"Time difference is {ms} milliseconds")

sec = delta.total_seconds()
print('difference in seconds:', sec)

min = sec / 60
print('difference in minutes:', min)

# get difference in hours
hours = sec / (60 * 60)
print('difference in hours:', hours)