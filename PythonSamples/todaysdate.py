from datetime import datetime
from datetime import date

todaydt = datetime.today()
print(todaydt)
todays_date_str = todaydt.strftime("%Y%m%d")
print(todays_date_str)