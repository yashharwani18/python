class Date:
    def __init__(self,day,month,year):
        self.date = [day,month,year]
    def __eq__(self,other):
        return self.date == other.date
    def __str__(self):
        return f"{self.date[0]}/{self.date[1]}/{self.date[2]}"
date1 = Date(22, 4, 2025)
date2 = Date(22, 4, 2025)
date3 = Date(23, 4, 2025)
print(f"date1 == date2: {date1 == date2}") 
print(f"date1 == date3: {date1 == date3}")
