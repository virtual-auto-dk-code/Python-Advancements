from datetime import datetime

date_str = '2023-02-28 14:30:00'
date_format = '%Y-%m-%d %H:%M:%S'

date_obj = datetime.strptime(date_str, date_format)
print(date_obj)