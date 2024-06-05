from datetime import datetime

date_string ="20240101"
x = datetime.strptime(date_string,"%Y%m%d")
#
# dt = datetime.now()
# print(type(dt))
import datetime

print((x + datetime.timedelta(days=0)).strftime("%Y%m%d"))