##  Fechas  ##

from datetime import datetime, time, date , timedelta

now = datetime.now()

def print_date(date):
  print("Day/Month/Year")
  print(f"{date.day}/{date.month}/{date.year}")


print_date(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


# timestamp = now.timestamp()
# print(timestamp)


year_2023 = datetime(2023,5,19)

print_date(year_2023)


# importanto time
print("--------- Usando time -----------")
current_time = time(1,23,20)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Usando date
print("--------- Usando date -----------")
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

other_date = date(current_date.year, current_date.month + 1,current_date.day)
print(other_date)


# timedelta se usa para trabajar con franjas de fechas
print("--------- Usando timedelta -----------")
init_timedelta = timedelta(500,200,100,weeks=20)
end_timedelta = timedelta(700,400,30,weeks=10)
print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)

