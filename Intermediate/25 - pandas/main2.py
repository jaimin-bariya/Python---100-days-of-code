import pandas as pd



mydf = pd.read_csv("25 - pandas\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240605.csv")

print(mydf.head(10))


colors = ["Gray", "Cinnomon", "Black"]


dic_color = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": []
}

for color in dic_color["colors"]:
    total_count = len(mydf[mydf["Primary Fur Color"] == color])
    dic_color["count"].append(total_count)


print(dic_color["count"])


newDF = pd.DataFrame(dic_color)

newDF.to_csv("fur_count.csv")

