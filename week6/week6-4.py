food = [
    ("Pasta", 150),
    ("Samosa", 20),
    ("Pizza", 300),
    ("Gulab Jamun", 80),
    ("Chole Bhature", 120),
    ("Pani Puri", 50)
]

food_swap = [(price,item) for item,price in food]
food_swap.sort(reverse=True)
sort_food = [(item,price) for price,item in food_swap]
for item in sort_food:
    print(item)