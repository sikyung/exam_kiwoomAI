from pandas import DataFrame
import datetime
# DataFrame = Excel sheet

data = [[100, 200, 300, 400],
        [200, 400, 500, 200]]

date = ["2021-03-01", "2021-02-26"]

index =[]

for i in date:
    day = datetime.datetime.strptime(i, "%Y-%m-%d")
    index.append(day)

columns = ['open', 'high', 'low', 'close']
df = DataFrame(data=data, columns=columns, index=index)
print(df)