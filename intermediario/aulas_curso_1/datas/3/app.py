from datetime import datetime

fmt = '%d/%m/%Y'

data = datetime.strptime('2024-02-26 09:40:00', '%Y-%m-%d %H:%M:%S')

print(data.strftime(fmt + ' %H:%M'))
print(data.strftime('%Y'), data.year)
