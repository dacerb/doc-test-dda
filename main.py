
import csv

with open('data.csv', "r") as f:
    file = csv.reader(f)

    header = next(file)
    data = []
    for row in file:
        iterable = zip(header,row)

        country_dict = {k: v for k, v in iterable}
        data.append(country_dict)

    print(data)
    data = list(filter(lambda item: item['pais'] == 'vzl', data))
    print(data)
    # https://stackoverflow.com/questions/2844516/how-to-filter-a-dictionary-according-to-an-arbitrary-condition-function


import pandas as pd

df = pd.read_csv("data.csv")
ata = df = df[df['pais'] == 'vzl']

print(ata['nombe'].values)