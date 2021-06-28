#!/usr/bin/env python3

import json
import jsonlines
from datetime import datetime

if __name__ == "__main__":
    with open("data/results.json", "r") as file:
        file = json.load(file)
        results = []
        for item in file['xml']['index']['item']:
            starts = str(datetime.strptime(item['datum'] + " " + item['von'], '%d.%m.%Y %H:%M').isoformat())
            ends = str(datetime.strptime(item['datum'] + " " + item['bis'], '%d.%m.%Y %H:%M').isoformat())

            results.append(
                {
                    "oid" : item['@original'],
                    "id" : item['id'],
                    "start": starts,
                    "end": ends,
                    "topic": item['thema'],
                    "zip": item['plz'],
                    "place": item['strasse_nr'],
                    "route": item['aufzugsstrecke']
                }
            )
        for result in results:
            print(json.dumps(result))
