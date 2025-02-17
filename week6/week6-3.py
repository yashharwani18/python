from datetime import date

date1 = (10, 2, 2023)
date2 = (25, 3, 2024)

d1 = date(date1[2], date1[1], date1[0])  
d2 = date(date2[2], date2[1], date2[0])
day = abs((d2-d1).days)

print(day)