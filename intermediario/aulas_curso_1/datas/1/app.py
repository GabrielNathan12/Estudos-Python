from datetime import datetime
from pytz import timezone


data  = datetime(2024, 2, 26, 8, 40)

print(data)

data_str = '2024/02/26 08:40:00'
data_str_fmt = '%Y/%m/%d %H:%M:%S'
data_br = '26/02/2024'
data_br_fmt = '%d/%m/%Y'

date = datetime.strptime(data_str,data_str_fmt)
print(date)

date_br = datetime.strptime(data_br,data_br_fmt)
print(date_br)


data_agr = datetime.now(timezone('Asia/Tokyo'))

print(data_agr)

d = datetime.now()

print(d.timestamp())

print(datetime.fromtimestamp(1708950325.476535))