class Weather:
    def __init__(self, *parameters):
        self.parameters = list(parameters)

    def __contains__(self, item):
        return item in self.parameters

weather_today = Weather("sunny", "windy", "dry")

print("sunny" in weather_today)  
print("rainy" in weather_today)  
 
