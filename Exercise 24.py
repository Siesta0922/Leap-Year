def is_leap(year)
  if year % 4 == 0:
    return "Leap Year"
  else:
    return "Not A Leap Year"
def days_in_month():
  month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

year = int(input("Year"))
month = int(input("Month"))
days = days_in_month(year,month)
print(days)
