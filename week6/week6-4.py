food = [
    ("Pasta", 150),
    ("Samosa", 20),
    ("Pizza", 300),
    ("Gulab Jamun", 80),
    ("Chole Bhature", 120),
    ("Pani Puri", 50)
]

import operator
food.sort(key=operator.itemgetter(1),reverse=True)

for item in food:
    print(item)

