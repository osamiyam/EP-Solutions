
import calendar

sum = 0
for year in range(1901, 2000+ 1):
    for month in range(1, 12 + 1):
        v = calendar.weekday(year, month, 1)
        print (year, month, v)
        if  v == 6: sum += 1
print sum
