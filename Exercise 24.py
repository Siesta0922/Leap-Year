def is_leap(year):
  if year % 4 == 0:
    return "Leap Year"
  else:
    return "Not A Leap Year"
def days_in_month(year,month):
    if is_leap(year) == "Leap Year":
        month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month <= len(month_days):
        str_year = str(year)
        str_days_month = str(month_days[month-1])
        return str_year + " " + str_days_month


year = int(input("Year : "))
month = int(input("Month : "))
days = days_in_month(year,month)
print(days)
print(is_leap(year))
