# import csv


# with open(file="25 - pandas\weather_data.csv") as f:

#     data = csv.reader(f)
#     tempretures = []

#     for row in data:
        
#         if row[1] == "temp":
#             continue
#         tempretures.append(int(row[1]))
    

# print(tempretures)



import pandas as pd

mydata = pd.read_csv("25 - pandas/weather_data.csv")
# print(mydata)





monday = mydata[mydata.day == "Monday"]
print(monday)

print(monday.temp[0])

temp_f = (monday.temp[0] * 9/5 ) + 32
print(temp_f)


mydata.to_csv("25 - pandas/new.csv")