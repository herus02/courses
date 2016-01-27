# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel).

def month_to_days(year, month):
  if month == 1 or month == 3 or month == 5 or month == 7:
  	return 31
  elif month == 8 or month == 10 or month == 12:
    return 31
  elif month == 4 or month == 6 or month == 9 or month == 11:
    return 30
  elif month == 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
  	return 29
  elif month == 2:
  	return 28
  else:
  	return 0

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	days = 0
	if year1 == year2:
		if month1 == month2:
			days = day2 - day1
		else:
			days = month_to_days(year1, month1) - day1
			print days
			month1 = month1 + 1
			while month1 < month2:
				days = days + month_to_days(year1, month1)
				month1 = month1 + 1
				print days
			days = days + day2
	else:
		days = month_to_days(year1, month1) - day1
		month1 = month1 + 1

		while month1 <= 12:
			days = days + month_to_days(year1, month1)
			month1 = month1 + 1

		month1, year1 = 1, year1 + 1
		while True:
			if year1 == year2:
				while month1 < month2:
					days = days + month_to_days(year1, month1)
					month1 = month1 + 1
				days = days + day2
				break
			else:
				while month1 <= 12:
					days = days + month_to_days(year1, month1)
					month1 = month1 + 1
				month1 = 1 				
				year1 = year1 + 1

	return days

print daysBetweenDates(2012,06,29,2013,06,30)