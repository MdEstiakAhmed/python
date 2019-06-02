import datetime
#show today's date
today1=datetime.date.today()	#datetime(module), date(class), today()(method)
print(today1)

print()
#show todays date and time
today2=datetime.datetime.today()
print(today2)

print()

today4=datetime.time()
print(today4)


print()


from datetime import datetime	#from datetime (module), import datetime (class)
today3=datetime.today()
print(today3)