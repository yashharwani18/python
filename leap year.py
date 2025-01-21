def is_leap_year(year):
    if year%4==0 and year %100!=0 or year %400==0:
        return f"{year} is leap year"
    else:
        return f"{year} is not leap year"


year = int(input("enter year"))
print(is_leap_year(year))

