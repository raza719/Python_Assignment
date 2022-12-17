import datetime
date=datetime.datetime.now()
day = date.day
month =  date.month
years =  date.year

print("today's date is {}-{}-{}".format(day,month,years))

if(date.hour>=12):
    print("current time is {}:{} PM".format(date.hour,date.minute))

else:
    print("current time is {}:{} AM".format(date.hour,date.minute))

