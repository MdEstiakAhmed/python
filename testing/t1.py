from datetime import datetime
import datetime
datetime_object = datetime.datetime.strptime('2019-06-01', '%Y-%m-%d')
today1 = datetime.datetime.today()
print(datetime_object, today1)
timedelta = (datetime_object - today1)
hours = timedelta.days*24
print(hours)



eventtimeck = content[5]
datetime_obj = datetime.datetime.strptime(eventtimeck, '%Y-%m-%d')
today1 = datetime.datetime.today()
print(datetime_obj, today1)
timedelta = (datetime_obj - today1)
hours = timedelta.days * 24
print(hours)