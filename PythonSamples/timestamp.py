from datetime import datetime
timestamp = (datetime.now()).timestamp()
date_time = datetime.fromtimestamp(timestamp)
str_date_time = date_time.strftime("%d%m%y_%H%M%S")
print("Current timestamp", str_date_time)