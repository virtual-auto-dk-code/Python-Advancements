from datetime import datetime, timezone, timedelta
from dateutil.relativedelta import relativedelta

# coff = datetime.now(timezone.utc) - timedelta()
# print(coff)

coff1 = datetime.now(timezone.utc) - relativedelta(months=2)  # current date time minus number of months
timezone_offset = timedelta(hours=5)  # timezone
# apply offset
dt_offset = coff1.replace(tzinfo=timezone(timezone_offset))  # format date time

print(dt_offset.isoformat())
iso_dt = dt_offset.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
print(dt_offset.isoformat())

now = datetime.now()
print(now)
# fmt = now.strftime("%Y-%m-%dT%H:%M:%SZ")
# print(fmt)

from datetime import datetime
now = datetime.now()
dt_out = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
print(dt_out)  # 2021-03-07T07:39:22Z

# --------------------------------------------------
from datetime import datetime
now = datetime.now()
dt_out = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
print(dt_out)  # 2021-03-07T07:39:22Z

coff1 = datetime.now() - relativedelta(months=24)  # current date time minus number of months
dt_out = coff1.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
print(dt_out)  # 2021-03-07T07:39:22Z
