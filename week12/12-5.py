class Time:
    def __init__(self,hours,minutes):
        self.hours =hours
        self.minutes=minutes
        self.normalize()  
    def normalize(self):
        if self.minutes>=60:
            self.hours+=self.minutes//60
            self.minutes = self.minutes%60
    def display(self):
        print(f"{self.hours}:{self.minutes}")
    def add_time(self, other):
        new_hours = self.hours + other.hours
        new_minutes = self.minutes + other.minutes
        result = Time(new_hours, new_minutes)
        return result
    def sub_time(self, other):
        new_hours = self.hours - other.hours
        new_minutes = self.minutes - other.minutes
        result = Time(new_hours, new_minutes)
        return result

t1=Time(2,45)
t2=Time(1,30)
t1.display()
t2.display()
result = t1.add_time(t2)
result.display()
result1 = t1.sub_time(t2)
result1.display()
        
