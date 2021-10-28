from datetime import datetime

#A datetime is an object composed by year, month, day, hour, minute, second, milisecond, etc

birthday = datetime(2001,11,16); #Year,month, day, hour, minute, second
print(birthday.day);
print(birthday.weekday())# 0-> monday; 1-> Tuesday; 2 -> Wednesday; 3-> Thursday; 4 -> Friday; 5 -> Saturday; 6 -> Sunday

print(datetime.now()) #Show this exactly moment datetime

print(datetime(2020,1,1) - datetime(2019,1,1)); #You can make opperations with the datetimes

parsed_date = datetime.strptime("Jan 15, 2019", "%b  %d, %Y"); # It's cappable to transform a date string (first parameter) according to the input parameter(the second one)
#THe correct correspondent parameter can be find in docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print(parsed_date);

date_string = datetime.strftime(datetime.now(), "%b %d, %Y") #It's the opposite of the .strptime(); It creates a string from a datetime parameter


