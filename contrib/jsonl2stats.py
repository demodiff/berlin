#!/usr/bin/egv python3

import json, csv
import pandas as pd 
from collections import Counter

with open("data/results.json", "r") as f:
    f = json.loads(f.read())
    zipcodes = [] 
    for item in f['index']:
        zipcodes.append(item['plz'])

    data = dict(Counter(zipcodes))
    data = sorted(data.items(), key=lambda item: item[1], reverse=True)
    with open("resources/zipcodes.csv", "r") as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        allzips = []
        dataframe = []
        for line in csvfile:
            allzips.append(line)
        for item in data:
            if item[0] == '':
                continue
            else:
                for line in allzips:
                    if line[0] == item[0]:
                        dataframe.append({"district": line[1], "zip": item[0], "count": item[1]})
        
        df = pd.DataFrame(dataframe)
        df.to_csv('data/stats-zips.csv')
