prices = {
    "apple": 20,
    "banana": 30,
    "milk": 50,
    "bread": 20,
    "eggs": 100
}
quantities = {
    "apple": 3,
    "banana": 2,
    "milk": 1,
    "bread": 2,
    "eggs": 1
}
sum1 = 0
for i in prices:
    sum1+=prices[i]*quantities[i]
        
print(sum1)