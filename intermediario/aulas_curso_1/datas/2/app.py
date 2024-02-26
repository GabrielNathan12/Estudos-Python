from datetime import datetime, timedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/2000 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2024 08:20:20', fmt)

#print(data_fim - data_inicio)

delta = timedelta(days=20)
print(delta.days, delta.seconds, delta.microseconds)
print(data_inicio + delta)