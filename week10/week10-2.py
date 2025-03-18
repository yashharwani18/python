import csv
data = {}

with open("data.csv", "r",newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        roll_no = row[0]
        name= row[1]
        sub1 = row[2]

        data[roll_no]={
            "name":name,
            "subject":sub1
        }

print(data)
