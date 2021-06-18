from datetime import datetime,timedelta,date


myday1 = date.fromisoformat('2020-11-23')
myday2 = date(2020,11,23) + timedelta(days=95)
myday1str = date.ctime(myday1)
myday2str = date.ctime(myday2)

print (myday1)
print(myday2)
print(myday1str)
print(myday2str)
print("end!")
