#!/usr/bin/env python3

import json
from datetime import datetime

if __name__ == "__main__":
    with open("data/results.json", "r") as file:
        file = json.loads(file.read())
        results = []
        for item in file['index']:
            starts = str(datetime.strptime(item['datum'] + " " + item['von'], '%d.%m.%Y %H:%M').isoformat())
            ends = str(datetime.strptime(item['datum'] + " " + item['bis'], '%d.%m.%Y %H:%M').isoformat())

            results.append(
                {
                    "id" : item['id'],
                    "start": starts,
                    "end": ends,
                    "topic": item['thema'],
                    "zip": item['plz'],
                    "place": item['strasse_nr'],
                    "route": item['aufzugsstrecke'],
                    "lfdnr": item['lfdnr']
                }
            )
        for result in results:
            print(json.dumps(result))
