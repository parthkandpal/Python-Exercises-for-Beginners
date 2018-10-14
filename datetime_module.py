#Dates, Times, Timedeltas, and Timezones
import datetime
import pytz #timezone
from tzlocal import get_localzone #to get local time zone
#datetime.date
date= datetime.date(2018,10,12)
print(date)

tday=datetime.date.today()
print(tday)

#weekday and isoweekday
print(tday.weekday())   #mon=0,sun=6
print(tday.isoweekday())#mon=,sun=7

#timedeltas

timedelta=datetime.timedelta(days=7)

print(tday+timedelta)  #adding timedelta
print(tday-timedelta)   #substracting timedelta

bday=datetime.date(2019,1,29)
till_bday=bday-tday
print(till_bday.days)

print(till_bday.total_seconds())



#datetime.time
#hr mins sec microsec
t= datetime.time(9,30,20,1000)
print(t)

#datetime.datetime

dt=datetime.datetime(2018,10,12,9,20,35,1000)

print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)


tdelta=datetime.timedelta(hours=12)

print(dt+tdelta)


#-----------------------
dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()

print(dt_today)  #returns local time
print(dt_now)   #can pass timezone as arg
print(dt_utcnow)

#pytz

dt=datetime.datetime(2018,10,12,6,5,20,3000,tzinfo=pytz.UTC)
print(dt)
dt_now=datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
#dt_utcnow= datetime.datetime.utcnow().replace(pytz.UTC)
print(dt_utcnow)




dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

'''
to get all timezones
import pytz
for i in pytz.all_timezones:
    print(i)'''

dt_singapore=dt_utcnow.astimezone(pytz.timezone('Singapore'))

print(dt_singapore)

#making local naive datetime timezone aware

local_dt=datetime.datetime.now()

local_timezone=get_localzone()
print(local_timezone)

local_dt=local_timezone.localize(local_dt)

dt_Katmandu=local_dt.astimezone(pytz.timezone('Asia/Katmandu'))

print(dt_Katmandu)


print(local_dt.isoformat())


#In 'strftime,' the 'f' is for 'format,' and in 'strptime,' the 'p' is for 'parse.' Knowing this helps you remember them better
print(local_dt.strftime('%B, %d, %y'))    #converts datetime to string
dt_str='January 29, 1997'
print(datetime.datetime.strptime(dt_str,'%B %d, %Y'))  #converts string to datetime



